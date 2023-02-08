from django.contrib import admin

# Register your models here.
from animal_app.models import Animals, AnimalShelter, Person, Avatar

admin.site.register(Animals)
admin.site.register(AnimalShelter)
admin.site.register(Person)
admin.site.register(Avatar)