from django.db import models

class Animals(models.Model):
    name = models.CharField(max_length=100)
    age = models.FloatField(max_length=3)
    adopted = models.BooleanField(default=False)
    breed = models.CharField(max_length=100)
    exotic = models.BooleanField(default=False)
    baby = models.BooleanField(default=False)

class AnimalShelter(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number= models.FloatField()
    postal_code = models.FloatField()
    province = models.CharField(max_length=100)
    contact_number = models.FloatField()

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.FloatField(max_length=3)
    dni = models.FloatField(max_length=15)
    house = models.CharField(max_length=50)





    def __str__(self):
        return self.name
