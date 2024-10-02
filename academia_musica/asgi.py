"""
ASGI config for academia_musica project.

It exposes the ASGI callable as a module-level variable named ``application``.


"""

import os # Importa el módulo os para interactuar con el sistema operativo

from django.core.asgi import get_asgi_application
# Establece la variable de entorno 'DJANGO_SETTINGS_MODULE' para que apunte a la configuración del proyecto 'academia_musica'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'academia_musica.settings')

# Obtiene la aplicación ASGI para el proyecto Django, permitiendo que se ejecute con servidores compatibles con ASGI
application = get_asgi_application()
