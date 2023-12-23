from django.db import models


# Create your models here.

class Schedule(models.Model):
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.location


class Feedback(models.Model):
    fullname = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    message = models.TextField()
    location = models.CharField(max_length=200, blank=True)
    phone_number = models.IntegerField(default=0)

    def __str__(self):
        return self.fullname

