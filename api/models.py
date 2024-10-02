from django.db import models
from django.core.exceptions import ValidationError
import re

# Validación personalizada para campos especificos de los formularios

def validate_alpha_space(value):
    # La expresión regular para validar letras (incluyendo tildes), espacios y comas
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ,]*$', str(value)):
        raise ValidationError('Este campo solo puede contener letras, espacios, comas y tildes.', code='invalid_alpha_space')

def validate_integer(value):
    if not str(value).isdigit():
        raise ValidationError('Este campo solo puede contener números enteros.', code='invalid_integer')

def validate_pack(value):
    if not re.match(r'^[a-zA-Z\s()]+$', value):
        raise ValidationError('Este campo solo puede contener letras, espacios y paréntesis.', code='invalid_pack')
    
def validate_two_decimal(value):
    if not re.match(r'^\d+(\.\d{1,2})?$', str(value)):
        raise ValidationError('Este campo solo puede contener números con hasta dos decimales.', code='invalid_decimal')
    
def validate_date_format(value):
    # La expresión regular para validar el formato dd/mm/yyyy
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', str(value)):
        raise ValidationError('La fecha debe estar en el formato dd/mm/yyyy y solo puede contener números y /.', code='invalid_date_format')

# Modelo para almacenar información de profesores    
class Teacher(models.Model):
    name = models.CharField(max_length=100, validators=[validate_alpha_space])

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Teacher' # Nombre de la tabla en la base de datos

class ClassPack(models.Model):
    name = models.CharField(max_length=100, validators=[validate_pack])

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Class_Pack'

class Instrument(models.Model):
    name = models.CharField(max_length=100, validators=[validate_alpha_space])

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Instrument'

class Price(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_two_decimal])
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.amount} - {self.description}"

    class Meta:
        db_table = 'Price'

class Class(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Class'

class Level(models.Model):
    name = models.CharField(max_length=100)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id')

    def __str__(self):
        return f"{self.name} - {self.class_id.name}"

    class Meta:
        db_table = 'Level'

class TeacherClass(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id')

    def __str__(self):
        return f"{self.teacher.name} - {self.class_id.name}"

    class Meta:
        db_table = 'Teacher_Class'

class Student(models.Model):
    first_name = models.CharField(max_length=100, validators=[validate_alpha_space])
    last_name = models.CharField(max_length=100, validators=[validate_alpha_space])
    age = models.IntegerField()
    phone = models.CharField(max_length=15, blank=True, null=True, validators=[validate_integer])
    email = models.EmailField(blank=True, null=True)
    family_discount = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'Student'

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, blank=True, null=True)
    enrollment_date = models.DateField()
    class_number = models.IntegerField(default=1)

    def __str__(self): # Este método es una representación textual legible del objeto
        return f"{self.student.first_name} {self.student.last_name} - {self.class_id.name}"

    class Meta:
        db_table = 'Enrollment'

class ClassPackDiscountRule(models.Model):
    class_pack = models.ForeignKey(ClassPack, on_delete=models.CASCADE)
    class_number = models.IntegerField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.class_pack.name} - {self.class_number}"

    class Meta:
        db_table = 'Class_Pack_Discount_Rule'

class ClassPackClass(models.Model):
    class_pack = models.ForeignKey(ClassPack, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id')

    def __str__(self):
        return f"{self.class_pack.name} - {self.class_id.name}"

    class Meta:
        db_table = 'Class_Pack_Class'