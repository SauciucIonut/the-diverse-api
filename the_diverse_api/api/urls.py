from django.urls import path
from .views import CatImagesLink, DogImagesLink, home, endpoints, doocumentation

urlpatterns = [
    path('api/animals/cats/', CatImagesLink.as_view()),
    path('api/animals/dogs/', DogImagesLink.as_view()),
    path('', home),
    path('endpoints/', endpoints),
    path('documentation/', doocumentation),
]
