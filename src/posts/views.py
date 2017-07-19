from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import PostModel, ImageModel

# Create your views here.

class IndexView(TemplateView):
    template_name = 'posts/posts_list.html'



class PostsListView(ListView):
    model = PostModel
    template_name = 'posts/posts_list.html'

    def get_context_data(self, **kwargs):
        context = super(PostsListView, self).get_context_data(**kwargs)
        image = ImageModel.objects.all().first()
        print(image)
        print(context)
        print(self.args)
        return context

class PostDetailView(DetailView):
    pass
