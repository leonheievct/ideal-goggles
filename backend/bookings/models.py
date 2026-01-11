from django.db import models
from users.models import Users
from properties.models import Property

# cоздаем журнал заказов

class Bookings(models.Model):
    # гость
    guest = models.ForeignKey(Users,on_delete=models.CASCADE)
    # объект
    object = models.ForeignKey(Property,on_delete=models.CASCADE)
    # дата заезда
    check_in_date = models.DateField(auto_now=True)
    # дата выезда
    departure_date = models.DateField(auto_now=True)
    # кол-во гостей
    number_of_guests = models.PositiveIntegerField()

    # итоговая цена
    final_price = models.PositiveIntegerField()
    # статус
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.guest

class BlockedDate(models.Model):
    object = models.ForeignKey(Property,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.object