from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    city_of_residence = models.CharField(max_length=40)

    def __str__(self):
        return self.name

