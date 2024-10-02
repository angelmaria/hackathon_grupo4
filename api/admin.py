
# Registrar modelos en el sitio de administración de Django
from django.contrib import admin
from .models import Teacher, ClassPack, Instrument, Price, Class, Level, TeacherClass, Student, Enrollment, ClassPackDiscountRule, ClassPackClass

admin.site.register(Teacher)
admin.site.register(ClassPack)
admin.site.register(Instrument)
admin.site.register(Price)
admin.site.register(Class)
admin.site.register(Level)
admin.site.register(TeacherClass)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(ClassPackDiscountRule)
admin.site.register(ClassPackClass)