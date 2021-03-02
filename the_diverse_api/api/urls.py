from django.urls import path
from . import views

urlpatterns = [
    # API endpoints
    path('api/animals/cats/', views.CatImagesLink.as_view(), name="api-animals-cats"),
    path('api/animals/dogs/', views.DogImagesLink.as_view(), name="api-animals-dogs"),
    
    # front-end 
    path('', views.home, name="index"),
    path('endpoints/', views.endpoints, name="endpoints"),
    path('documentation/', views.documentation, name="documentation"),

    # page to see the token
    path('token/', views.tokenpage, name="tokenpage"),

    # user registration, login and logout
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
]
