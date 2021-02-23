from django.urls import path
from .views import cats_all

urlpatterns = [
    path('animals/cats/', cats_all),
]
