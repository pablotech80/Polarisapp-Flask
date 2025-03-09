"""
Módulo principal de la aplicación Polaris App.

Este módulo inicia la aplicación Flask y define todas las rutas necesarias
para la gestión de usuarios y clientes, incluyendo autenticación y CRUD.

Autor: Pablo Techera
Versión: 1.0
"""

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Cliente
from forms import LoginForm, ClienteForm

# Inicializar la aplicación Flask
app = Flask(__name__)
app.config.from_object('config.Config')

# Inicializar la base de datos y el gestor de login
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirige a /login si el usuario no está autenticado


@login_manager.user_loader
def load_user(user_id):
    """
    Carga un usuario a partir de su ID en la base de datos.

    Args:
        user_id (int): ID del usuario.

    Returns:
        User: Objeto del usuario autenticado o None si no se encuentra.
    """
    return db.session.get(User, int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Maneja la autenticación de usuarios en la aplicación.

    Returns:
        str: Renderiza la plantilla de login o redirige al listado de clientes si el usuario está autenticado.
    """
    if current_user.is_authenticated:
        return redirect(url_for('listar_clientes'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('listar_clientes'))
        flash('Usuario o contraseña incorrectos.', 'danger')

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    """
    Cierra la sesión del usuario actual y lo redirige a la página de login.

    Returns:
        str: Redirección a la página de login con un mensaje flash.
    """
    logout_user()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('login'))


@app.route('/clientes')
@login_required
def listar_clientes():
    """
    Muestra la lista de clientes registrados en la base de datos.

    Returns:
        str: Renderiza la plantilla `clientes.html` con la lista de clientes.
    """
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)


@app.route('/clientes/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_cliente():
    """
    Crea un nuevo cliente en la base de datos.

    Returns:
        str: Renderiza el formulario de creación o redirige a la lista de clientes tras guardar.
    """
    form = ClienteForm()
    if form.validate_on_submit():
        cliente = Cliente(
            nombre=form.nombre.data,
            codigo=form.codigo.data,
            telefono1=form.telefono1.data,
            direccion=form.direccion.data,
            nif=form.nif.data
        )
        db.session.add(cliente)
        db.session.commit()
        flash('Cliente creado exitosamente.', 'success')
        return redirect(url_for('listar_clientes'))
    return render_template('form_cliente.html', form=form)


@app.route('/clientes/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_cliente(id):
    """
    Edita la información de un cliente existente.

    Args:
        id (int): ID del cliente a editar.

    Returns:
        str: Renderiza el formulario de edición o redirige a la lista de clientes tras actualizar.
    """
    cliente = Cliente.query.get_or_404(id)
    form = ClienteForm(obj=cliente)
    if form.validate_on_submit():
        form.populate_obj(cliente)
        db.session.commit()
        flash('Cliente actualizado correctamente.', 'success')
        return redirect(url_for('listar_clientes'))
    return render_template('form_cliente.html', form=form)


@app.route('/clientes/eliminar/<int:id>', methods=['POST'])
@login_required
def eliminar_cliente(id):
    """
    Elimina un cliente de la base de datos.

    Args:
        id (int): ID del cliente a eliminar.

    Returns:
        str: Redirige a la lista de clientes tras eliminar con un mensaje flash.
    """
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    flash('Cliente eliminado correctamente.', 'danger')
    return redirect(url_for('listar_clientes'))


@app.route('/')
def home():
    """
    Redirige al usuario a la lista de clientes si está autenticado, de lo contrario, al login.

    Returns:
        str: Redirección a la lista de clientes o a la página de login.
    """
    if current_user.is_authenticated:
        return redirect(url_for('listar_clientes'))
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, port=9999)
