from django.contrib import admin
from django.urls import path
from animal_app.views import animal_list, put_up_for_adoption, create_shelter, shelter_list, create_profile, profile_list, contact_number, AnimalDelete, AnimalUpdate, login_request, register
from adoption_web.views import index_hi


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_hi, name="index"),
    path("putup-adoption/", put_up_for_adoption),
    path("animal-list/", animal_list),
    path("create-shelter/", create_shelter),
    path("shelter-list/", shelter_list),
    path("create-profile/", create_profile),
    path("profile-list/", profile_list),
    path("adopted/", contact_number),
    path("delete-animal/<int:pk>/", AnimalDelete.as_view()),
    path("update-animal/<int:pk>", AnimalUpdate.as_view()),
    path("login/", login_request, name = "Login"),
    path("register/", register, name = "Register"),
]
