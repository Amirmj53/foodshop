from django.urls import path
from . import views


app_name = "reservation"

urlpatterns = [
    path("", views.reserv, name="book"),
    path("succes/", views.succes, name="succes")
]
