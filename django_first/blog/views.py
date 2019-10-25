
#from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

#import Post from models, it is our real database


#pretend that this collection is coming from a database

# posts = [
# 			{
# 				'author': 'Marjorie Ivy',
# 				'title' : 'Blog Post 1',
# 				'content': 'First',
# 		 		'date_posted': 'October 21, 2019'
# 		 	},
# 		 	{
# 		 		'author': 'Marjorie Moreno',
# 		 		'title': 'Blog Post 2',
# 		 		'content': 'Second',
# 		 		'date_posted': 'October 22, 2019'
# 		 	}
# 		]

# Create your views here.
#render returns http requests
def home(request):
	context = {
			'posts': Post.objects.all()
		}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})