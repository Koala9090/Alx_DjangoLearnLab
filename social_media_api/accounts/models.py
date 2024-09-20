from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True,null=True)
    profile_picture = models.ImageField(upload_to='profile_photos/', null=True,blank=True)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followers', blank=True,symmetrical=False)
    def __str__(self):
        return self.username
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)