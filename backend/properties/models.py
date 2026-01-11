from django.db import models
from users.models import Users

# создаем класс удобства

class Amenity(models.Model):
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

    



# Создаем класс собственности

class Property(models.Model):
    # хозяин
    owner = models.ForeignKey(Users,on_delete=models.CASCADE)
    # тип собственности
    type = models.CharField(max_length=50)
    # название
    title = models.CharField(max_length=50)
    # описание
    description = models.TextField(blank=True)
    # адресс
    address = models.CharField(max_length=50)
    # координаты
    coordinates = models.CharField(max_length=50)
    # цена за ночь
    price_per_night = models.PositiveIntegerField()
    # правила
    rules = models.CharField(max_length=50)
    # удобства
    conveniences = models.ManyToManyField(Amenity)

    def __str__(self):
        return self.owner

