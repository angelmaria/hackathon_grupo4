# Importa el módulo de serialización de Django REST Framework y los modelos de la aplicación
from rest_framework import serializers
from .models import Ciudad, Categoria, Subcategoria, Documento

# Serializador para el modelo Ciudad
class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'

# Serializador para el modelo Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

# Serializador para el modelo Subcategoria
class SubcategoriaSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)  # Incluye los detalles de la categoría

    class Meta:
        model = Subcategoria
        fields = '__all__'

# Serializador para el modelo Documento
class DocumentoSerializer(serializers.ModelSerializer):
    ciudad = CiudadSerializer(read_only=True)  # Incluye los detalles de la ciudad
    categoria = CategoriaSerializer(read_only=True)  # Incluye los detalles de la categoría
    # subcategoria = SubcategoriaSerializer(read_only=True)  # Si deseas incluir los detalles de la subcategoría

    class Meta:
        model = Documento
        fields = '__all__'
