from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path("", views.publicdata, name="publicdata"),
]