from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Animals(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    adopted = models.BooleanField(default=True)
    breed = models.CharField(max_length=100)
    exotic = models.BooleanField(default=False)
    baby = models.BooleanField(default=False)
    image = models.ImageField(upload_to=('pets/'), default="default.jpg")

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

class ContactNumber(models.Model):
    contact_number = models.IntegerField()

    def __str__(self):
        return self.name

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="avatar")
    image = models.ImageField(upload_to="icons", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user} - {self.image}"