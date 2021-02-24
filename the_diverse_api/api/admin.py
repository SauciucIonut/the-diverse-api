from django.contrib import admin
from .models import CatImage, DogImage

# Register your models here.

admin.site.register(CatImage)
admin.site.register(DogImage)