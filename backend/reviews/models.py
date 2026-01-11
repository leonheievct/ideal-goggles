from django.db import models
from properties.models import Property

# cоздаем класс "комментарии"

class Reviews(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
    property = models.ForeignKey(Property,on_delete=models.CASCADE)

    def __str__(self):
        return self.date
    
 