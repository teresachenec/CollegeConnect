from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField
from django.urls import reverse_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
	user = AutoOneToOneField(User, on_delete="CASCADE")
	major = models.TextField(blank="")
	interest = models.TextField(blank="")

class CollegeConnect(models.Model):
	profile = models.ForeignKey(to = Profile, on_delete="CASCADE")

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()
