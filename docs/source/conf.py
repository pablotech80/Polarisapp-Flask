import os
import sys
sys.path.insert(0, os.path.abspath('../..'))  # Asegura que Sphinx vea los módulos

# Extensiones para mejorar la documentación
extensions = [
    'sphinx.ext.autodoc',        # Extrae docstrings de Python
    'sphinx.ext.napoleon',       # Soporta docstrings estilo Google y NumPy
    'sphinx.ext.viewcode',       # Agrega enlaces al código fuente
]

# Configurar el tema de la documentación
html_theme = 'sphinx_rtd_theme'
