from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank = True)
    userimage = models.URLField(max_length=5000, blank = True)
    description = models.TextField(max_length=500, blank = True)
    twitter = models.URLField(max_length=200,blank=True)
    instagram = models.URLField(max_length=200,blank=True)
    website = models.URLField(max_length=200,blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()