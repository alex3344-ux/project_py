from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
CITY_NAME_CHOICES = [
    ('RU', 'Россия'),
    ('UZ', 'Узбекистан'),
]

class City(models.Model):
    country = models.CharField(verbose_name='Страна', default=CITY_NAME_CHOICES[0], choices=CITY_NAME_CHOICES, blank=True, null=True, max_length=3)
    name = models.CharField(max_length=100)

    about_city = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.name} - {self.country} - {self.about_city}'




