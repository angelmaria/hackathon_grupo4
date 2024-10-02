# Importa el módulo de serialización de Django REST Framework y los modelos de la aplicación
from rest_framework import serializers
from .models import Teacher, ClassPack, Instrument, Price, Class, Level, TeacherClass, Student, Enrollment, ClassPackDiscountRule, ClassPackClass

# Serializador para el modelo Teacher
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


# Serializador para el modelo ClassPack
class ClassPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPack
        fields = '__all__'

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class TeacherClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherClass
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class ClassPackDiscountRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPackDiscountRule
        fields = '__all__'

class ClassPackClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPackClass
        fields = '__all__' #indica que todos los campos del modelo asociado deben ser incluidos en la serialización