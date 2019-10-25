from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


#this is the database
# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now) #use this to be able to change dates.
#auto_now_add=True date time only when post is creaed
	author = models.ForeignKey(User, on_delete=models.CASCADE) #when user is deleted post should be deleted too

	def __str__(self):
		return self.title