from django.shortcuts import render, get_object_or_404
from django.utils.crypto import get_random_string

from .models import Teacher


# Create your views here.
def view_teachers(request, pk=None) -> render:
    if 'create' in request.path:
        kravtz = Teacher.objects.filter(first_name='Кравец')
        if not kravtz:
            Teacher.objects.create(
                first_name='Кравец',
                last_name='Боб',
                birth_day='2000-12-15',
                email='bob@kravetz.eau',
                phone='+998901002030'
            )
        else:
            teacher_tmp = Teacher.objects.filter(first_name='Кравец').first()
            teacher_tmp.last_name = get_random_string(length=15, allowed_chars='АБВГДЕЁЖЗИКЛМНОПРСТУФХЧШЩЭЮЯ')
            teacher_tmp.email = get_random_string(length=6,
                                                  allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789') + '@kravetz.eau'
            teacher_tmp.phone = "+" + get_random_string(length=13, allowed_chars='0123456789')
            teacher_tmp.save()

    if pk:
        current_teacher = get_object_or_404(Teacher, pk=pk)
        template = 'teacher_detail.html'
        context = {
            'current_teacher': current_teacher,
        }
    else:
        teachers = Teacher.objects.all()
        template = 'teachers.html'
        context = {
            'teachers': teachers,
        }

    return render(request=request, template_name=template, context=context)
