from django.contrib import admin
from django.urls import path
from animal_app.views import animal_list, put_up_for_adoption, create_shelter, shelter_list, create_profile, profile_list, contact_number, AnimalDelete, AnimalUpdate, login_request, register, profile_edit, about_us
from adoption_web.views import index_hi
from django.contrib.auth.views import LogoutView
from adoption_web.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

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
    path("logout/", LogoutView.as_view(template_name="logout.html"), name = "Logout"),
    path("profile-edit/", profile_edit, name="Editar Perfil"),
    path("about-us/", about_us),
]+ static(MEDIA_URL, document_root = MEDIA_ROOT)