from django.db import models

# Create your models here.

class Animals(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    adopted = models.BooleanField(default=False)
    breed = models.CharField(max_length=100)
    exotic = models.BooleanField(default=False)
    baby = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class AnimalShelter(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number= models.IntegerField()
    postal_code = models.IntegerField()
    province = models.CharField(max_length=100)
    shelter_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dni = models.IntegerField()
    house_type = models.CharField(max_length=50)


    def __str__(self):
        return self.name