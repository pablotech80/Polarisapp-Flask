from app import app, db
from models import User
from werkzeug.security import generate_password_hash

with app.app_context():
    db.create_all()
    # Crear usuario admin
    admin = User(username='admin', password=generate_password_hash('admin'))
    db.session.add(admin)
    db.session.commit()
    print("Base de datos y usuario admin creados")
