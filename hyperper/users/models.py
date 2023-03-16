from django.db import models

class Event(models.Model):
    name = models.CharField('name', max_length=200)
    password = models.CharField('password', max_length=200)

    def __str__(self):
        return self.name


# Create your models here.
