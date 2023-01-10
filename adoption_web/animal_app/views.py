from django.shortcuts import render
from animal_app.forms import AnimalForm, ShelterForm, PersonForm
from animal_app.models import Animals, AnimalShelter, Person
# Create your views here.


def put_up_for_adoption(request):
    if request.method == "GET":
        context = {
            "form": AnimalForm()
        }
        return render(request, "putup-adoption.html", context=context)

    elif request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            Animals.objects.create(
                name = form.cleaned_data["name"],
                age = form.cleaned_data["age"],
                adopted = form.cleaned_data["adopted"],
                breed = form.cleaned_data["breed"],
                exotic = form.cleaned_data["exotic"],
                baby = form.cleaned_data["baby"],
            )
            context = {
                "message": "¡Aviso creado!"
            }
            return render(request, "putup-adoption.html", context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form": AnimalForm()
            }
            return render(request, "putup-adoption.html", context=context)

def animal_list(request):
    if "search" in request.GET:
        search = request.GET["search"]
        all_animals = Animals.objects.filter(name_icontains=search)
    else:
        all_animals = Animals.objects.all()
    context = {
        "adoptions":all_animals,
    }
    return render(request, "animal-list.html", context = context)