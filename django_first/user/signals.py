#to avoid getting into admin to change their profiles, this signals can be used by django
#to avoid side effects of import
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#we want to get the post_save signal
#user is the sender
#then create a receiver
#we want a user profile to be created to each new profile

@receiver(post_save, sender=User) #when a user is saved, send this user
def create_profile(sender,instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User) #when a user is saved, send this user
def save_profile(sender,instance, **kwargs):
		instance.profile.save()


