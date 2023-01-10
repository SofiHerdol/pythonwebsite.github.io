"""adoption_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from animal_app.views import animal_list, put_up_for_adoption
from adoption_web.views import index_hi

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_hi, name="index"),
    path("putup-adoption/", put_up_for_adoption),
    path("animal-list/", animal_list),
]
