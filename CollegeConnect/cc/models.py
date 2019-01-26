from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your models here.
class Users(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    major = models.TextField()
    interest = models.TextField()


