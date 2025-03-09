"""
Módulo de modelos de la base de datos para Polaris App.

Este módulo define las clases `User` y `Cliente` para la gestión
de usuarios y clientes en la base de datos utilizando SQLAlchemy.

Autor: Pablo Techera
Versión: 1.0
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# Inicializa SQLAlchemy
db = SQLAlchemy()


class User(db.Model, UserMixin):
    """
    Modelo de usuario para la autenticación en la aplicación.

    Atributos:
        id (int): Identificador único del usuario.
        username (str): Nombre de usuario único.
        password (str): Contraseña encriptada del usuario.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Cliente(db.Model):
    """
    Modelo de cliente que almacena la información de cada cliente registrado.

    Atributos:
        id (int): Identificador único del cliente.
        nombre (str): Nombre completo del cliente.
        codigo (str): Código único que identifica al cliente.
        telefono1 (str, opcional): Número de teléfono principal del cliente.
        direccion (str, opcional): Dirección del cliente.
        nif (str, opcional): Número de identificación fiscal del cliente.
    """
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(50), unique=True, nullable=False)
    telefono1 = db.Column(db.String(20))
    direccion = db.Column(db.String(200))
    nif = db.Column(db.String(20))
