from django.urls import path
from .views import CatsLink

urlpatterns = [
    path('animals/cats/', CatsLink.as_view()),
]
