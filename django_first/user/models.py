from django.contrib.auth.models import User
from django.db import models
from PIL import Image

#create your profile to have one to one relationship
#one profile - one login
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	#cascade will delete the profile if profile is deleted
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	#after this, run makemigrations
# install pip install Pillow - this is for images
#run makemigrations again
#run migrate to create the table

	def save(self):
		super().save()
		#grab and resize. Use Pillow
		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)