import pytest
from .models import Ciudad, Categoria, Subcategoria, Documento

# Test para crear una Ciudad
@pytest.mark.django_db
def test_create_ciudad():
    ciudad = Ciudad.objects.create(nombre='Madrid')  # Cambiar 'name' a 'nombre'
    assert Ciudad.objects.count() == 1  # Verifica que se ha creado una Ciudad
    assert ciudad.nombre == 'Madrid'  # Verifica que el nombre de la Ciudad es correcto

@pytest.mark.django_db
def test_create_categoria():
    categoria = Categoria.objects.create(nombre='Música')  # Cambiar 'name' a 'nombre'
    assert Categoria.objects.count() == 1
    assert categoria.nombre == 'Música'  # Cambiar 'name' a 'nombre'

@pytest.mark.django_db
def test_create_subcategoria():
    categoria = Categoria.objects.create(nombre='Arte')  # Cambiar 'name' a 'nombre'
    subcategoria = Subcategoria.objects.create(nombre='Pintura', categoria=categoria)  # Cambiar 'name' a 'nombre'
    assert Subcategoria.objects.count() == 1
    assert str(subcategoria) == 'Pintura'  # Cambiar 'Pintura - Arte' a 'Pintura'

@pytest.mark.django_db
def test_create_documento():
    ciudad = Ciudad.objects.create(nombre='Barcelona')  # Crear la Ciudad
    categoria = Categoria.objects.create(nombre='Documentación')  # Crear la Categoria
    documento = Documento.objects.create(titulo='Documentación de Proyecto', ciudad=ciudad, categoria=categoria)  # Pasar categoria
    assert Documento.objects.count() == 1
    assert documento.titulo == 'Documentación de Proyecto'  # Verifica el título
    assert documento.ciudad == ciudad  # Verifica la ciudad
    assert documento.categoria == categoria  # Verifica la categoría

