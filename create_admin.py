from app import app, db
from models import User
from werkzeug.security import generate_password_hash

with app.app_context():
	admin = User.query.filter_by(username = 'admin').first()
	if admin:
		admin.password = generate_password_hash('admin')
		print("Contraseña de admin actualizada.")
	else:
		admin = User(username = 'admin', password = generate_password_hash('admin'))
		db.session.add(admin)
		print("Usuario admin creado con contraseña 'admin'.")

	db.session.commit()

