from django.urls import path
from .views import CatImagesLink, DogImagesLink, home, endpoints, documentation, loginpage, register, logoutUser

urlpatterns = [
    path('api/animals/cats/', CatImagesLink.as_view(), name="api-animals-cats"),
    path('api/animals/dogs/', DogImagesLink.as_view(), name="api-animals-dogs"),
    path('', home, name="index"),
    path('endpoints/', endpoints, name="endpoints"),
    path('documentation/', documentation, name="documentation"),
    path('login/', loginpage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('register/', register, name="register"),
]
