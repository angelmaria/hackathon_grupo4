# Registrar modelos en el sitio de administración de Django
from django.contrib import admin
from .models import Ciudad, Documento, Categoria, Subcategoria

# Registro de modelos en el panel de administración
@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created_at', 'updated_at')
    search_fields = ('nombre', 'pais')

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ciudad', 'categoria', 'created_at', 'updated_at')
    search_fields = ('titulo',)
    list_filter = ('ciudad', 'categoria')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created_at', 'updated_at')
    search_fields = ('nombre',)

@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'created_at', 'updated_at')
    search_fields = ('nombre',)
    list_filter = ('categoria',)
