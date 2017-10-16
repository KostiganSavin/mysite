from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import PostModel, ImageModel

# Create your views here.

class IndexView(TemplateView):
    template_name = 'posts/posts_list.html'


class PostsListView(ListView):
    model = PostModel
    template_name = 'posts/posts_list.html'


class PostDetailView(DetailView):
    model = PostModel
    template_name = "posts/post_detail.html"
