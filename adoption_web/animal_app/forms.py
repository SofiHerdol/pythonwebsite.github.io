from django import forms

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

class PersonForm(forms.Form):
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

class NewContactNumber(forms.Form):
    contact_number = forms.IntegerField()
