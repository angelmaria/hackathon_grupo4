# Importación de viewsets de Django REST framework
from rest_framework import viewsets

# Importación de modelos de la aplicación
from .models import Teacher, ClassPack, Instrument, Price, Class, Level, TeacherClass, Student, Enrollment, ClassPackDiscountRule, ClassPackClass

# Importación de serializadores de la aplicación
from .serializers import TeacherSerializer, ClassPackSerializer, InstrumentSerializer, PriceSerializer, ClassSerializer, LevelSerializer, TeacherClassSerializer, StudentSerializer, EnrollmentSerializer, ClassPackDiscountRuleSerializer, ClassPackClassSerializer

# Importación de funciones útiles para vistas en Django
from django.shortcuts import render, redirect, get_object_or_404

# Importación de formularios definidos en la aplicación
from .forms import EnrollmentForm, StudentForm, TeacherForm, InstrumentForm, ClassPackForm, PriceForm

# Importación de módulos de Django para manejar errores y conexiones a la base de datos
from django import forms
from django.db import connection
from django.db import IntegrityError
from django.core.exceptions import ValidationError

# Definición de rutas a plantillas HTML específicas
delete_url = "api/confirm_delete.html"
edit_pack = "api/edit_class_pack.html"

# Definición de conjuntos de vistas para modelos específicos usando viewsets
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ClassPackViewSet(viewsets.ModelViewSet):
    queryset = ClassPack.objects.all()
    serializer_class = ClassPackSerializer

class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class TeacherClassViewSet(viewsets.ModelViewSet):
    queryset = TeacherClass.objects.all()
    serializer_class = TeacherClassSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class ClassPackDiscountRuleViewSet(viewsets.ModelViewSet):
    queryset = ClassPackDiscountRule.objects.all()
    serializer_class = ClassPackDiscountRuleSerializer

class ClassPackClassViewSet(viewsets.ModelViewSet):
    queryset = ClassPackClass.objects.all()
    serializer_class = ClassPackClassSerializer

# Vista para la página principal, mostrando todos los registros de los modelos
def home(request):
    context = {
        'teachers': Teacher.objects.all(),
        'class_packs': ClassPack.objects.all(),
        'instruments': Instrument.objects.all(),
        'prices': Price.objects.all(),
        'classes': Class.objects.all(),
        'levels': Level.objects.all(),
        'teacher_classes': TeacherClass.objects.all(),
        'students': Student.objects.all(),
        'enrollments': Enrollment.objects.all(),
        'class_pack_discounts': ClassPackDiscountRule.objects.all(),
        'class_pack_classes': ClassPackClass.objects.all(),
    }
    return render(request, 'api/home.html', context) # La función render genera una respuesta HTTP utilizando una plantilla HTML ('api/home.html') y el contexto proporcionado

# Vista para crear una inscripción
def create_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('home')
        except IntegrityError as e:
            print(f"Error de integridad al crear la inscripción: {e}")
        except Exception as e:
            print(f"Error al crear la inscripción: {e}")
    else:
        form = EnrollmentForm()

    context = {'form': form}
    return render(request, 'api/create_enrollment.html', context)

# Vista para crear un estudiante
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('home')
        except IntegrityError as e:
            print(f"Error de integridad al crear el estudiante: {e}")
            form.add_error(None, "Error de integridad al guardar el estudiante.")
        except Exception as e:
            print(f"Error al crear el estudiante: {e}")
            form.add_error(None, "Error al guardar el estudiante.")
    else:
        form = StudentForm()

    context = {
        'form': form,
    }
    return render(request, 'api/create_student.html', context)

# Vista para crear un instrumento
def create_instrument(request):
    if request.method == 'POST':
        form = InstrumentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except IntegrityError as e:
                print(f"Error de integridad al crear el instrumento: {e}")
                form.add_error(None, "Error de integridad al guardar el instrumento.")
    else:
        form = InstrumentForm()

    context = {
        'form': form,
    }
    return render(request, 'api/create_instrument.html', context)

# Vista para crear un profesor
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('home')
        except IntegrityError as e:
            # Aquí puedes personalizar el manejo de la excepción según tus necesidades
            print(f"Error al guardar el profesor: {e}")
            form.add_error(None, 'Error al guardar el profesor. Por favor, verifica los datos e intenta nuevamente.')

    else:
        form = TeacherForm()

    context = {
        'form': form,
    }
    return render(request, 'api/create_teacher.html', context)

# Vista para eliminar un profesor
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        try:
            teacher.delete()
            return redirect('home')
        except IntegrityError as e:
            print(f"Error al eliminar el profesor: {e}")
           #redirige a una página de error
            return redirect('error_page')  # Reemplaza 'error_page' con el nombre de tu vista de error

    context = {
        'object_type': 'profesor',
        'teacher': teacher
    }
    return render(request, delete_url, context)

# Vista para eliminar un instrumento
def delete_instrument(request, instrument_id):
    instrument = get_object_or_404(Instrument, id=instrument_id)
    if request.method == 'POST':
        instrument.delete()
        return redirect('home')  # Ajusta 'home' según el nombre de tu vista principal
    context = {
        'object_type': 'instrumento',
        'instrument': instrument
    }
    return render(request, delete_url, context)

# Vista para eliminar un estudiante
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('home')  # Ajusta 'home' según el nombre de tu vista principal
    context = {
        'object_type': 'alumno',
        'teacher': student
    }
    return render(request, delete_url, context)

# Vista para editar un profesor
def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        try:
            if form.is_valid():
                form.save()
                return redirect('home')
        except IntegrityError as e:
            # Manejo de errores de integridad
            print(f"Error al editar el profesor: {e}")
            form.add_error(None, 'Error al guardar los cambios. Por favor, verifica los datos e intenta nuevamente.')
    
    else:
        form = TeacherForm(instance=teacher)
    
    context = {
        'form': form,
    }
    return render(request, 'api/edit_teacher.html', context)

# Vista para crear un paquete de clases
def create_class_pack(request):
    if request.method == 'POST':
        form = ClassPackForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('home')
        except Exception as e:
            # Aquí puedes manejar el error como desees
            print(f"Error al crear el paquete de clases: {e}")
            form.add_error(None, 'Error al guardar el paquete de clases. Por favor, verifica los datos e intenta nuevamente.')
    else:
        form = ClassPackForm()
    
    return render(request, 'api/create_class_pack.html', {'form': form})

# Vista para editar un instrumento
def edit_instrument(request, instrument_id):
    instrument = get_object_or_404(Instrument, id=instrument_id)
    if request.method == 'POST':
        form = InstrumentForm(request.POST, instance=instrument)
        try:
            if form.is_valid():
                form.save()
                return redirect('home')
        except ValidationError as e:
            # Se maneja el error de validación específico
            print(f"Error de validación al editar el instrumento: {e}")
            form.add_error(None, str(e))
        except Exception as e:
            # Aquí puedes manejar otros tipos de excepciones
            print(f"Error al editar el instrumento: {e}")
            form.add_error(None, 'Error al guardar los cambios. Por favor, verifica los datos e intenta nuevamente.')
    else:
        form = InstrumentForm(instance=instrument)
    
    return render(request, 'api/edit_instrument.html', {'form': form})

# Vista para editar un paquete de clases
def edit_class_pack(request, pk):
    class_pack = get_object_or_404(ClassPack, pk=pk)
    
    if request.method == 'POST':
        try:
            form = ClassPackForm(request.POST, instance=class_pack)
            if form.is_valid():
                # Validar que no se seleccionen más de 4 instrumentos
                selected_instruments = form.cleaned_data['instruments']
                if len(selected_instruments) > 4:
                    raise ValueError("No se permiten más de 3 instrumentos en un paquete de clases.")
                
                # Guardar el formulario si es válido
                form.save()
                
                return redirect('home')
        
        except ValueError as ve:
            # Manejar el error específico de violación de regla de negocio
            form = ClassPackForm(instance=class_pack)
            context = {
                'form': form,
                'error_message': str(ve)
            }
            return render(request, edit_pack, context)
        
        except Exception as e:
            # Manejar  excepciones genéricas
            form = ClassPackForm(instance=class_pack)
            context = {
                'form': form,
                'error_message': f"Error al guardar el formulario: {str(e)}"
            }
            return render(request, edit_pack , context)

    else:
        form = ClassPackForm(instance=class_pack)

    context = {
        'form': form,
    }
    return render(request, edit_pack, context)

# Vista para editar un estudiante
def edit_student(request, student_id):
    try:
        student = get_object_or_404(Student, id=student_id)
        if request.method == 'POST':
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = StudentForm(instance=student)
    except Student.DoesNotExist:
        return render(request, 'api/error.html', {'error_message': 'Estudiante no encontrado'})
    return render(request, 'api/edit_student.html', {'form': form})

# Vista para eliminar un paquete de clases
def delete_class_pack(request, pk):
    class_pack = get_object_or_404(ClassPack, pk=pk)
    if request.method == 'POST':
        class_pack.delete()
        return redirect('home')
    context = {
    'object_type': 'paquete de clases',  # Especifica aquí el tipo de objeto que estás eliminando
    'class_pack': class_pack
    }
    return render(request, delete_url, context)

# Vista para editar un precio
def edit_price(request, pk):
    price = get_object_or_404(Price, pk=pk)
    if request.method == 'POST':
        form = PriceForm(request.POST, instance=price)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PriceForm(instance=price)
    return render(request, 'api/edit_price.html', {'form': form, 'price': price})

# Vista para ejecutar una consulta SQL personalizada y mostrar resultados por mes
def execute_query_month(request):
    with connection.cursor() as cursor:
        # Configurar el idioma español para la conexión
        cursor.execute("SET lc_time_names = 'es_ES';")
        
        # Ejecutar la consulta principal
        cursor.execute("""
            SELECT
                DATE_FORMAT(e.enrollment_date, '%m-%Y') AS `Mes de inscripción`,
                COUNT(*) AS `Total Inscripciones`,
                GROUP_CONCAT(DISTINCT CONCAT(s.first_name, ' ', s.last_name, ' (', sub.count_per_student, ')') ORDER BY s.last_name SEPARATOR ', ') AS `Estudiantes inscritos`
            FROM
                Enrollment e
            JOIN
                Student s ON e.student_id = s.id
            JOIN (
                SELECT student_id, DATE_FORMAT(enrollment_date, '%m-%Y') AS enrollment_month, COUNT(*) AS count_per_student
                FROM Enrollment
                GROUP BY student_id, DATE_FORMAT(enrollment_date, '%m-%Y')
            ) sub ON e.student_id = sub.student_id AND DATE_FORMAT(e.enrollment_date, '%m-%Y') = sub.enrollment_month
            GROUP BY
                DATE_FORMAT(e.enrollment_date, '%m-%Y')
            ORDER BY
                `mes de inscripción`;
        """)
        columns = [col[0] for col in cursor.description]
        data = cursor.fetchall()

    return render(request, 'api/query_results_month.html', {'columns': columns, 'data': data})

# Vista para ejecutar una consulta SQL personalizada y mostrar el total de deudas
def execute_query_total_due(request):
    with connection.cursor() as cursor:
        # Ejecutar la nueva consulta
        cursor.execute("""
            SELECT 
                s.first_name AS Nombre,
                s.last_name AS Apellidos,
                CONCAT(FORMAT(
                    SUM(
                        CASE 
                            WHEN e.class_number = 1 THEN 
                                p.amount  -- Primera clase, sin descuento
                            WHEN e.class_number = 2 THEN 
                                p.amount * 0.5  -- Segunda clase, 50% descuento
                            WHEN e.class_number >= 3 THEN 
                                p.amount * 0.25  -- Tercera o más, 75% descuento
                            ELSE 
                                p.amount  -- Caso por defecto (sin descuento)
                        END * 
                        (CASE 
                            WHEN s.family_discount = TRUE THEN 0.9  -- Aplica un 10% de descuento adicional si hay descuento familiar
                            ELSE 1  -- Sin descuento adicional
                        END)
                    ), 2
                ), ' €') AS "Total Deuda"
            FROM 
                Student s
            JOIN 
                Enrollment e ON s.id = e.student_id
            JOIN 
                Class c ON e.class_id = c.id
            JOIN 
                Price p ON c.price_id = p.id
            GROUP BY 
                s.id, s.first_name, s.last_name
            ORDER BY 
                s.last_name, s.first_name;
        """)
        columns = [col[0] for col in cursor.description]
        data = cursor.fetchall()

    return render(request, 'api/query_results_total_due.html', {'columns': columns, 'data': data})
