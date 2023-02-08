from django.contrib import admin

# Register your models here.
from animal_app.models import Animals, AnimalShelter, UserProfile

admin.site.register(Animals)
admin.site.register(AnimalShelter)
admin.site.register(UserProfile)