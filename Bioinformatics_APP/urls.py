from django.urls import path, include, re_path
from . import views
from django.contrib import admin


urlpatterns = [
    re_path("^$", views.publicdata, name="publicdata"),
    path('admin/', admin.site.urls),
]
