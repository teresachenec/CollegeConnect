from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField
from django.urls import reverse_lazy

# Create your models here.
class CollegeConnect(models.Model):
	profile = models.ForeignKey(to = Profile, on_delete="CASCADE")

class Profile(models.Model):
	user = AutoOneToOneField(User, on_delete="CASCADE")
	name = models.TextField()

class Skill(models.Model):

class Groups(models.Model):

class Classes(models.Model):

class Questions(models.Model):

class Tutors(models.Model):
