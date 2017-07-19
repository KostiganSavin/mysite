from django.conf.urls import url
from .views import IndexView, AboutMeView

urlpatterns = [
    #url(r'^$', IndexView.as_view(), name='about'),
    url(r'^$', AboutMeView.as_view(), name='aboutme'),
]
