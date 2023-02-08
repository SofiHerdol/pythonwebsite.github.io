from django.shortcuts import render
from animal_app.forms import AnimalForm, ShelterForm, PersonForm, NewContactNumber, UserRegisterForm, UserEditForm
from animal_app.models import Animals, AnimalShelter, Person, ContactNumber, Avatar
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate



def put_up_for_adoption(request):
    if request.method == "GET":
        context = {
            "form": AnimalForm()
        }
        return render(request, "putup-adoption.html", context=context)

    elif request.method == "POST":
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            Animals.objects.create(
                name = form.cleaned_data["name"],
                age = form.cleaned_data["age"],
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
        all_animals = Animals.objects.filter(name__icontains=search)
    else:
        all_animals = Animals.objects.all()
    context = {
        "adoptions":all_animals,
    }
    return render(request, "animal-list.html", context = context)

def create_shelter(request):
    if request.method == "GET":
        context = {
            "form": ShelterForm()
        }
        return render(request, "create-shelter.html", context=context)
    elif request.method == "POST":
        form = ShelterForm(request.POST)
        if form.is_valid():
            AnimalShelter.objects.create(
                name = form.cleaned_data["name"],
                street = form.cleaned_data["street"],
                number= form.cleaned_data["number"],
                postal_code = form.cleaned_data["postal_code"],
                province = form.cleaned_data["province"],
                shelter_type = form.cleaned_data["shelter_type"],
            )
            context = {
                "message": "¡Refugio creado!"
            }
            return render(request, "create-shelter.html", context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form": ShelterForm()
            }
            return render(request, "create-shelter.html", context=context)

def shelter_list(request):
    if "search" in request.GET:
        search = request.GET["search"]
        all_shelters = AnimalShelter.objects.filter(name_icontains=search)
    else:
        all_shelters = AnimalShelter.objects.all()
    context = {
        "shelters":all_shelters,
    }
    return render(request, "shelter-list.html", context = context)

def create_profile(request):
    if request.method == "GET":
        context = {
            "form": PersonForm()
        }
        return render(request, "create-profile.html", context=context)
    elif request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            Person.objects.create(
                name = form.cleaned_data["name"],
                age = form.cleaned_data["age"],
                dni= form.cleaned_data["dni"],
                house_type = form.cleaned_data["house_type"],
            )
            context = {
                "message": "¡Perfil creado!"
            }
            return render(request, "create-profile.html", context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form": PersonForm()
            }
            return render(request, "create-profile.html", context=context)

def profile_list(request):
    if "search" in request.GET:
        search = request.GET["search"]
        all_profiles = Person.objects.filter(name_icontains=search)
    else:
        all_profiles= Person.objects.all()
    context = {
        "profiles":all_profiles,
    }
    return render(request, "profile-list.html", context = context)

def contact_number(request):
    if request.method == "GET":
        context = {
            "form": NewContactNumber()
        }
        return render(request, "adopted.html", context=context)
    elif request.method == "POST":
        form = NewContactNumber(request.POST)
        if form.is_valid():
            ContactNumber.objects.create(
                contact_number = form.cleaned_data["contact_number"],
            )
            context = {
                "message": "¡En breves nos estaremos comunicando con vos para darte más información!"
            }
            return render(request, "adopted.html", context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form": NewContactNumber()
            }
            return render(request, "adopted.html", context=context)

class AnimalDelete(DeleteView):
    model = Animals
    template_name = "delete-animal.html"
    success_url = "/animal-list/"

class AnimalUpdate(UpdateView):
    model = Animals
    fields = ["name", "age", "breed", "gender", "adopted", "exotic", "baby"]
    template_name = "update-animal.html"
    success_url = "/animal-list/"

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)


            if user is not None:
                login(request, user)

                return render(request, "index.html", {"mensaje":f"¡Bienvenidx, {username}!"})
            else:
                return render(request, "index.html", {"mensaje":f"¡Ups! Datos incorrectos :("})
        
        else:
            return render(request, "index.html", {"mensaje":f"¡Ups! Formulario incorrecto :("})
    
    form = AuthenticationForm()

    return render(request, "login.html", {"form":form})

def register(request):
    if request.method == "GET":
        form = UserRegisterForm()
        context = {
            "form":form
        }
        return render(request, "register.html", context=context)

    elif request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form.username = form.cleaned_data["username"]
            form.email = form.cleaned_data["email"]
            form.password1 = form.cleaned_data ["password1"]
            form.password2 = form.cleaned_data ["password2"]
            form.save()
            return render(request, "index.html", {"mensaje":"Usuario creado :)"})
    else:
        form = UserRegisterForm
    return render(request, "register.html", {"form":form})

def profile_edit(request):
    username = request.user

    if request.method == "POST":
        myform = UserEditForm(request.POST)
        if myform.is_valid:
            info = myform.cleaned_data

            username.email = info["email"]
            username.password1 = info["password1"]
            username.password2 = info["password2"]
            username.save()

            return render(request, "index.html")
    
    else:
        myform = UserEditForm(initial={"email":request.user.email})
    return render(request, "profile-edit.html", {"myform":myform, "username":username})

def avatar_url(request):
    icons = Avatar.objects.filter(user=request.user.id)
    return render(request, "index.html", {"avatar":icons[0].image.url})

def about_us(request):
    return render(request, "about_us.html")









