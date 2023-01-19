from django.db import models

# Create your models here.


class Ice_cream(models.Model):
    name = models.CharField(max_length=100)
    sort_of = models.TextField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.sort_of} - {self.price}'


class Market(models.Model):
    date_of_created = models.DateField()
    name_market = models.CharField(max_length=100)
    over = models.TextField(max_length=100)
    geo = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.date_of_created} - {self.name_market} - {self.over} - {self.geo}'
