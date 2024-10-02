import pytest
from .models import Teacher, ClassPack, Instrument, Price, Class, Level, TeacherClass, Student, Enrollment, ClassPackDiscountRule, ClassPackClass

# Test para crear un Teacher
@pytest.mark.django_db
def test_create_teacher():
    teacher = Teacher.objects.create(name='John Doe')
    assert Teacher.objects.count() == 1# Verifica que se ha creado un Teacher
    assert teacher.name == 'John Doe'  # Verifica que el nombre del Teacher es correcto

@pytest.mark.django_db
def test_create_class_pack():
    class_pack = ClassPack.objects.create(name='Pack 1')
    assert ClassPack.objects.count() == 1
    assert class_pack.name == 'Pack 1'

@pytest.mark.django_db
def test_create_instrument():
    instrument = Instrument.objects.create(name='Piano')
    assert Instrument.objects.count() == 1
    assert instrument.name == 'Piano'

@pytest.mark.django_db
def test_create_class():
    instrument = Instrument.objects.create(name='Guitar')
    price = Price.objects.create(amount=35.00, description='Beginner Class Price')
    _class = Class.objects.create(name='Guitar Beginner', instrument=instrument, price=price)
    assert Class.objects.count() == 1
    assert _class.name == 'Guitar Beginner'

@pytest.mark.django_db
def test_create_level():
    instrument = Instrument.objects.create(name='Violin')
    price = Price.objects.create(amount=40.00, description='Intermediate Class Price')
    _class = Class.objects.create(name='Violin Intermediate', instrument=instrument, price=price)
    level = Level.objects.create(name='Intermediate Level', class_id=_class)
    assert Level.objects.count() == 1
    assert str(level) == 'Intermediate Level - Violin Intermediate'

@pytest.mark.django_db
def test_create_teacher_class():
    teacher = Teacher.objects.create(name='Jane Smith')
    instrument = Instrument.objects.create(name='Flute')
    price = Price.objects.create(amount=35.00, description='Advanced Class Price')
    _class = Class.objects.create(name='Flute Advanced', instrument=instrument, price=price)
    teacher_class = TeacherClass.objects.create(teacher=teacher, class_id=_class)
    assert TeacherClass.objects.count() == 1
    assert str(teacher_class) == 'Jane Smith - Flute Advanced'

@pytest.mark.django_db
def test_create_student():
    student = Student.objects.create(first_name='Alice', last_name='Johnson', age=25)
    assert Student.objects.count() == 1
    assert str(student) == 'Alice Johnson'

@pytest.mark.django_db
def test_create_enrollment():
    student = Student.objects.create(first_name='Bob', last_name='Brown', age=30)
    instrument = Instrument.objects.create(name='Drums')
    price = Price.objects.create(amount=35.00, description='Advanced Class Price')
    _class = Class.objects.create(name='Drums Advanced', instrument=instrument, price=price)
    enrollment = Enrollment.objects.create(student=student, class_id=_class, enrollment_date='2024-07-10')
    assert Enrollment.objects.count() == 1
    assert str(enrollment) == 'Bob Brown - Drums Advanced'

@pytest.mark.django_db
def test_create_class_pack_discount_rule():
    class_pack = ClassPack.objects.create(name='Class Pack B')
    discount_rule = ClassPackDiscountRule.objects.create(class_pack=class_pack, class_number=3, discount_percentage=10.00)
    assert ClassPackDiscountRule.objects.count() == 1
    assert str(discount_rule) == 'Class Pack B - 3'

@pytest.mark.django_db
def test_create_class_pack_class():
    class_pack = ClassPack.objects.create(name='Class Pack C')
    instrument = Instrument.objects.create(name='Bass Guitar')
    price = Price.objects.create(amount=40.00, description='Intermediate Class Price')
    _class = Class.objects.create(name='Bass Guitar Intermediate', instrument=instrument, price=price)
    class_pack_class = ClassPackClass.objects.create(class_pack=class_pack, class_id=_class)
    assert ClassPackClass.objects.count() == 1
    assert str(class_pack_class) == 'Class Pack C - Bass Guitar Intermediate'
