from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AnimalForm(forms.Form):
    gender_choices = (
        ("Macho" , "Macho"),
        ("Hembra", "Hembra"),
    )
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=gender_choices)
    breed = forms.CharField(max_length=100)
    exotic = forms.BooleanField(required=False)
    baby = forms.BooleanField(required=False)
    image = forms.ImageField()

class ShelterForm(forms.Form):
    shelter_choices = (
        ("Refugio" , "Refugio"),
        ("Casa de tránsito" , "Casa de tránsito"),
        ("Otro", "Otro"),
    )
    name = forms.CharField(max_length=100)
    street = forms.CharField(max_length=100)
    number= forms.FloatField()
    postal_code = forms.FloatField()
    province = forms.CharField(max_length=100)
    shelter_type = forms.ChoiceField(choices=shelter_choices)
    image = forms.ImageField()

class UserUpdateForm(forms.Form):
    house_choices = (
        ("Casa" , "Casa"),
        ("Departamento" , "Departamento"),
        ("Otro", "Otro"),
    )
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    dni = forms.IntegerField()
    house_type = forms.ChoiceField(choices=house_choices)
    contact_number = forms.IntegerField(required=False)

class UserRegisterForm(UserCreationForm):
    house_choices = (
        ("Casa" , "Casa"),
        ("Departamento" , "Departamento"),
        ("Otro", "Otro"),
    )
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    dni = forms.IntegerField()
    house_type = forms.ChoiceField(choices=house_choices)
    contact_number = forms.IntegerField(required=False)
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ["username", "name", "email",  "age", "dni", "house_type", "contact_number", "image","password1", "password2"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

