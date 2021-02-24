from django.urls import path
from .views import CatImagesLink, DogImagesLink

urlpatterns = [
    path('animals/cats/', CatImagesLink.as_view()),
    path('animals/dogs/', DogImagesLink.as_view()),
]
