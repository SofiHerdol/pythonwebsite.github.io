
from django.contrib import admin
from django.urls import path
from animal_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", index_hi),
    path("putup-adoption/", put_up_for_adoption),
    path("animal-list/", animal_list),
]
