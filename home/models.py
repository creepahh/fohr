from django.db import models


# Create your models here.

class Schedule(models.Model):
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.location

