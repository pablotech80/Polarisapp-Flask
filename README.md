# Polaris App 🚀

Polaris App es una aplicación web desarrollada con **Flask** para la gestión de clientes.  
Incluye autenticación de usuarios y un CRUD completo para administrar los clientes de manera sencilla.  

📌 **Esta versión está desarrollada en Flask**.

---

## 📌 Tecnologías Utilizadas

- **Python** (Flask)
- **Flask-SQLAlchemy** (ORM para la base de datos)
- **Flask-Login** (Autenticación de usuarios)
- **Flask-WTF** (Formularios seguros con validaciones)
- **Sphinx** (Documentación automática)
- **Bootstrap** (Interfaz simple y moderna)

---

## 🚀 Instalación y Configuración

### 1️⃣ Clonar el Repositorio  
```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO

```

### 2️⃣ Crear y Activar el Entorno Virtual
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate  # Windows

```
### 3️⃣ Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar la Base de Datos
```bash
python db_init.py
python populate_db.py  # (Opcional) Insertar datos de prueba
```
### 5️⃣ Ejecutar la Aplicación
```bash 
python app.py

La aplicación estará disponible en http://localhost:9999 🌍
```

### 🔑 Autenticación

Para acceder al sistema, usa el siguiente usuario por defecto:
Usuario: admin
Contraseña: admin

### 📖 Documentación

La documentación completa está generada con Sphinx.
Para visualizarla, genera los archivos HTML:

```bash
cd docs
make html
```
Luego, abre docs/build/html/index.html en tu navegador.

### 🛠 Rutas de la Aplicación

| Método  | Ruta                     | Descripción |
|---------|--------------------------|-------------|
| `GET`   | `/`                      | Redirección a login o clientes |
| `GET`   | `/login`                  | Página de inicio de sesión |
| `POST`  | `/login`                  | Autenticación de usuario |
| `GET`   | `/logout`                 | Cerrar sesión |
| `GET`   | `/clientes`               | Lista de clientes |
| `GET`   | `/clientes/nuevo`         | Formulario para agregar cliente |
| `POST`  | `/clientes/nuevo`         | Crear cliente |
| `GET`   | `/clientes/editar/<id>`   | Formulario de edición de cliente |
| `POST`  | `/clientes/editar/<id>`   | Guardar cambios del cliente |
| `POST`  | `/clientes/eliminar/<id>` | Eliminar cliente |

### 📌 Contribuir

Si quieres mejorar esta aplicación, haz un fork, crea una nueva rama y envía un Pull Request.
¡Cualquier mejora es bienvenida! 🚀

### 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.

