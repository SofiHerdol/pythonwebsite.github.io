from django.contrib import admin
from animal_app.models import Animals

@admin.register(Animals)
class AnimalsAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "breed", "adopted")
    list_filter = ("age", "adopted")
    search_fields = ("name", )