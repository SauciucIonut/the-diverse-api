from django.urls import path
from .views import CatImagesLink, DogImagesLink, home

urlpatterns = [
    path('api/animals/cats/', CatImagesLink.as_view()),
    path('api/animals/dogs/', DogImagesLink.as_view()),
    path('', home),
]
