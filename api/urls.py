from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import CiudadViewSet, DocumentoViewSet, CategoriaViewSet, SubcategoriaViewSet, home

# Instancia un DefaultRouter para manejar las rutas de los ViewSet
router = DefaultRouter()
router.register(r'ciudad', CiudadViewSet)  # Ruta para Ciudad
router.register(r'documento', DocumentoViewSet)  # Ruta para Documento
router.register(r'categoria', CategoriaViewSet)  # Ruta para Categoria
router.register(r'subcategoria', SubcategoriaViewSet)  # Ruta para Subcategoria

urlpatterns = [
    path('api/', include(router.urls)),  # Rutas registradas por los ViewSet
    path('', home, name='home'),  # Ruta para la vista home
    path('filtered/', views.filtered_view, name='filtered_view'),
    path('create-ciudad/', views.create_ciudad, name='create_ciudad'),  # Crear una ciudad
    path('create-documento/', views.create_documento, name='create_documento'),  # Crear un documento
    path('delete-ciudad/<int:ciudad_id>/', views.delete_ciudad, name='delete_ciudad'),  # Eliminar ciudad
    path('edit-ciudad/<int:ciudad_id>/', views.edit_ciudad, name='edit_ciudad'),  # Editar ciudad
    path('delete-documento/<int:documento_id>/', views.delete_documento, name='delete_documento'),  # Eliminar documento
    path('edit-documento/<int:documento_id>/', views.edit_documento, name='edit_documento'),  # Editar documento
    path('create-categoria/', views.create_categoria, name='create_categoria'),  # Crear una categoría
    path('create-subcategoria/', views.create_subcategoria, name='create_subcategoria'),  # Crear una subcategoría
    path('delete-categoria/<int:categoria_id>/', views.delete_categoria, name='delete_categoria'),  # Eliminar categoría
    path('edit-categoria/<int:categoria_id>/', views.edit_categoria, name='edit_categoria'),  # Editar categoría
    path('delete-subcategoria/<int:subcategoria_id>/', views.delete_subcategoria, name='delete_subcategoria'),  # Eliminar subcategoría
    path('edit-subcategoria/<int:subcategoria_id>/', views.edit_subcategoria, name='edit_subcategoria'),  # Editar subcategoría
]

# Si estás en modo DEBUG, agrega configuraciones para manejar archivos de medios
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Configuración para manejar archivos de medios
