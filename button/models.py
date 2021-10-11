from django.db import models

# Create your models here.


class Button(models.Model):
    name = 'Кнопка'
    title = 'ВКЛ/ВЫКЛ'
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name
