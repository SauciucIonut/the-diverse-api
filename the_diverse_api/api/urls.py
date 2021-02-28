from django.urls import path
from .views import CatImagesLink, DogImagesLink, home, endpoints, documentation, login, register

urlpatterns = [
    path('api/animals/cats/', CatImagesLink.as_view()),
    path('api/animals/dogs/', DogImagesLink.as_view()),
    path('', home),
    path('endpoints/', endpoints),
    path('documentation/', documentation),
    path('login/', login),
    path('register/', register),
]
