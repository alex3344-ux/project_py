from django.db import models
from .validators.validators import validate_age


# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=150)
    second_name = models.CharField(verbose_name='Фамилия', max_length=150)
    birth_day = models.DateField(verbose_name='Дата рождения', validators=[validate_age])
    email = models.EmailField(verbose_name='e-mail')
    phone = models.CharField(verbose_name='Телефон', max_length=11)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

        ordering = ['first_name', 'second_name']

    def __str__(self):
            return f'{self.first_name} {self.second_name}'

