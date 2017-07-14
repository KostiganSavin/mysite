from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index_view(request):
    context = {}
    return render(request, 'base.html', context)


class IndexView(TemplateView):
    template_name = 'base.html'
