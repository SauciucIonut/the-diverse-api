from django.urls import path
from .views import CatImagesLink

urlpatterns = [
    path('animals/cats/', CatImagesLink.as_view()),
]
