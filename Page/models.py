from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Funnel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=False)
    body = RichTextField(max_length=500000,blank=False)
    description = models.TextField(max_length=5000,blank=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.title} || {self.user.username}'

    def get_absolute_url(self):
        return reverse('funnel', kwargs={'pk': self.pk})