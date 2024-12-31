from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path("home", views.Home, name= "home"),
    re_path("publicdata", views.publicdata, name="publicdata"),
]