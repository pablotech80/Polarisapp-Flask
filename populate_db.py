from app import app, db
from models import Cliente

clientes_data = [
    {"nombre": "Juan Pérez", "codigo": "JP001", "telefono1": "123456789", "direccion": "Calle Falsa 123", "nif": "12345678A"},
    {"nombre": "Ana Gómez", "codigo": "AG002", "telefono1": "987654321", "direccion": "Av. Central 456", "nif": "87654321B"},
    {"nombre": "Carlos López", "codigo": "CL003", "telefono1": "654123987", "direccion": "Plaza Mayor 789", "nif": "34567890C"}
]

with app.app_context():
    for data in clientes_data:
        # Verifica si el cliente ya existe
        cliente_existente = Cliente.query.filter_by(codigo=data["codigo"]).first()
        if not cliente_existente:
            cliente = Cliente(**data)
            db.session.add(cliente)

    db.session.commit()
    print("Clientes de prueba añadidos o ya existentes.")
