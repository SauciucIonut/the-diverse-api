from django.urls import path
from .views import CatImagesLink, DogImagesLink, home, endpoints, documentation, login, register

urlpatterns = [
    path('api/animals/cats/', CatImagesLink.as_view(), name="api-animals-cats"),
    path('api/animals/dogs/', DogImagesLink.as_view(), name="api-animals-dogs"),
    path('', home, name="index"),
    path('endpoints/', endpoints, name="endpoints"),
    path('documentation/', documentation, name="documentation"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
]
