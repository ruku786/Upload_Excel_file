from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    # birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)

# Create your models here.
