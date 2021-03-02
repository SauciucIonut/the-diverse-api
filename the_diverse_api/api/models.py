from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group

# API MODELS ----------------------------------------

class CatImage(models.Model):
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.link

class DogImage(models.Model):
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.link

# TOKEN MODEL ---------------------------------------
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        Group.objects.get(name='free').user_set.add(instance)