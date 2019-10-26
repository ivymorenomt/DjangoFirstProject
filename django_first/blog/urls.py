from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), # postlistview will not work if as_view isn't called.
    path('about/', views.about, name='blog-about'),
]

#<app>/<model>_<viewtype>.html