from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
import re
from .validators import validate_address_length


# GENDER = [
#     (None, 'Не определено'),
#     (1, 'Мужчина'),
#     (0, 'Женщина'),
# ]

# Create your models here.
class BasePerson(models.Model):
    class PersonGenderChoice(models.IntegerChoices):
        MALE = 1, _('Мужчина')
        FEMALE = 0, _('Женщина')
        __empty__ = _('Не определено')

    name = models.CharField(verbose_name='Имя', max_length=255, blank=True, null=True)
    age = models.IntegerField(verbose_name='Возраст', default=1, blank=True, null=True)
    gender = models.BooleanField(verbose_name='Пол',
                                 default=PersonGenderChoice.MALE, choices=PersonGenderChoice.choices, blank=True,
                                 null=True)
    adress = models.CharField(verbose_name='Адресс', max_length=255, blank=True, null=True)

    name = models.CharField(verbose_name='Имя', max_length=255, blank=True, null=True,
                            validators=[RegexValidator(
                                regex='^\D+$',
                                message = "Введите пожалуйста строку",
                                flags=re.IGNORECASE,
                            )])
    adress = models.CharField(verbose_name='Адрес', max_length=255, blank=True, null=True,
                              validators=[validate_address_length])

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.name == "Irod":
            return # Irod is not accepted name
        else:
            super().save(*args, **kwargs)



class Human(BasePerson):
    NAME_TERMS_CHOICES = [
        ('Basic', (
            ('mr', 'Mr'),
            ('ms', 'Ms'),
        )
         ),
        ('Prof', (
            ('dr', 'Dr'),
            ('sir', 'Sir'),
        )
         ),
        ('uncknown', 'Uncknown')
    ]

    name_terms = models.CharField(verbose_name='Обращение', default=NAME_TERMS_CHOICES[1][1],
                                  choices=NAME_TERMS_CHOICES, max_length=255)

    def get_absolute_url(self):
        return f'/human/person/{self.pk}'


class Meta:
    verbose_name = 'Человек'
    verbose_name_verbose = 'Люди'

    ordering = ['pk', ]
    get_latest_by = ['-age', ]

    constraints = [
        models.CheckConstraint(check=models.Q(age_qte=16), name='age'),
    ]


class Children(models.Model):
    parent_field = models.ManyToManyField(Human, through='PersonRelationShip')
    age = models.IntegerField(verbose_name='Возраст', default=1, blank=True, null=True)
    fio = models.CharField(max_length=100)

    age = models.IntegerField(verbose_name='Возраст', default=1, blank=True, null=True,
                              validators=[MinValueValidator(0), MaxValueValidator(15)])



class PersonRelationShip(models.Model):
    parent = models.ForeignKey(Human, on_delete=models.CASCADE)
    child = models.ForeignKey(Children, on_delete=models.CASCADE)

    def __str__(self) -> str:
        # return f'Родитель {self.parent.name} - Ребенок: {self.child.name}'
        return f'Родитель {self.parent} - Ребенок: {self.child}'

    class Meta:
        verbose_name = 'Отношения'
        verbose_name_plural = 'Отношения'
        unique_together = ['child']

