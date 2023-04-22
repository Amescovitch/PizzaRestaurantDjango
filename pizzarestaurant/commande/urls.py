from django.urls import path
from . import  views

app_name = "commande"

urlpatterns = [
    path('', views.commande, name="index"),
]
