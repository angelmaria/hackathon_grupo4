# Importa AppConfig, la clase base para la configuración de aplicaciones en Django
from django.apps import AppConfig

 # Define la configuración de la aplicación 'api'
class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Especifica el tipo de campo auto-incremental por defecto
    name = 'api' #se define el nombre de la app
