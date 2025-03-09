"""
Módulo de formularios para Polaris App.

Este módulo define los formularios para la autenticación de usuarios y
la gestión de clientes utilizando Flask-WTF y WTForms.

Autor: Pablo Techera
Versión: 1.0
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    """
    Formulario de inicio de sesión para los usuarios.

    Atributos:
        username (StringField): Campo de entrada para el nombre de usuario.
        password (PasswordField): Campo de entrada para la contraseña del usuario.
        submit (SubmitField): Botón para enviar el formulario.
    """
    username = StringField('Usuario', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')


class ClienteForm(FlaskForm):
    """
    Formulario para la gestión de clientes.

    Atributos:
        nombre (StringField): Nombre completo del cliente (obligatorio).
        codigo (StringField): Código único del cliente (obligatorio).
        telefono1 (StringField, opcional): Número de teléfono del cliente.
        direccion (StringField, opcional): Dirección del cliente.
        nif (StringField, opcional): Número de identificación fiscal del cliente.
        submit (SubmitField): Botón para enviar el formulario.
    """
    nombre = StringField('Nombre', validators=[DataRequired()])
    codigo = StringField('Código', validators=[DataRequired()])
    telefono1 = StringField('Teléfono')
    direccion = StringField('Dirección')
    nif = StringField('NIF')
    submit = SubmitField('Guardar')
