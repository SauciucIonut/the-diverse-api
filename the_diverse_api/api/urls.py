from django.urls import path
from .views import cats

urlpatterns = [
    path('animals/cats/', cats),
]
