from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ciudad'  # Nombre exacto de la tabla en la base de datos

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categoria'  # Nombre exacto de la tabla en la base de datos

    def __str__(self):
        return self.nombre

class Subcategoria(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, related_name='subcategorias', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'subcategoria'  # Nombre exacto de la tabla en la base de datos

    def __str__(self):
        return self.nombre

class Documento(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    ciudad = models.ForeignKey(Ciudad, related_name='documentos', on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, related_name='documentos', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'documento'  # Nombre exacto de la tabla en la base de datos

    def __str__(self):
        return self.titulo
