
#from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)

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

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts' #call the context in the hometemplate
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post

#the LoginRequiredMixin will avoid a user from creating a post or accessing the url directly without logging in
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	#override
	def form_valid(self, form):
		form.instance.author = self.request.user #take instance and set author equal to user
		return super().form_valid(form)

#UserPassesTestMixin prevents a different user to update someone's post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	#override
	def form_valid(self, form):
		form.instance.author = self.request.user #take instance and set author equal to user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author: #if current user is the author then, return true, else false
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/' #to avoid ImproperlyConfigured at /post/7/delete/ No URL to redirect to. Provide a success_url.

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author: #if current user is the author then, return true, else false
			return True
		return False


def about(request):
	return render(request, 'blog/about.html', {'title':'About'})