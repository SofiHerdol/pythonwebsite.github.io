from django import forms

class AnimalForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    adopted = forms.BooleanField()
    breed = forms.CharField(max_length=100)
    exotic = forms.BooleanField()
    baby = forms.BooleanField()

class ShelterForm(forms.Form):
    shelter_choices = (
        ("Refugio" , "Refugio"),
        ("casa de tránsito" , "casa de tránsito"),
        ("otros", "otros"),
    )
    name = forms.CharField(max_length=100)
    street = forms.CharField(max_length=100)
    number= forms.FloatField()
    postal_code = forms.FloatField()
    province = forms.CharField(max_length=100)
    shelter_type = forms.ChoiceField(choices=shelter_choices)

class PersonForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    dni = forms.IntegerField()
    house = forms.CharField(max_length=50)