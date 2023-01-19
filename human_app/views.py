from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import BasePerson, Human, Children, PersonRelationShip


def index(request, pk) -> render:
    """ Вывод данных из таблицы Movie отсортированных
        по убыванию по полю pk
    """
    template_ = 'person.html'
    current_person = Human.objects.get(pk=pk)
    persons = Human.objects.all()

    context = {
        'current_person': current_person,
        'persons': persons,
    }

    return render(request, template_, context=context)