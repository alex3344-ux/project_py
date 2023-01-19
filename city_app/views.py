from django.shortcuts import render
from .models import City


def index(request, pk) -> render:
    """ Вывод данных из таблицы отсортированных
        по убыванию по полю pk
    """
    template_ = 'view_city.html'
    current_city = City.objects.get(pk=pk)
    cities = City.objects.all()

    # context = {
    #     'city': current_city
    # }
    context = {
        'city': cities
    }

    return render(request, template_, context=context)








