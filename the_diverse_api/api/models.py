from django.db import models

# Create your models here.

class Cats(models.Model):
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.link

class Dogs(models.Model):
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.link