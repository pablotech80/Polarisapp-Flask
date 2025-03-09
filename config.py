import os

class Config:
    SECRET_KEY = 'clave_secreta'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  # Usa SQLite en lugar de PostgreSQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
