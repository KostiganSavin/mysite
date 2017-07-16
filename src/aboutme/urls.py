from django.conf.urls import url
from .views import IndexView, AboutMeView, ContastsView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='about'),
    url(r'^aboutme/$', AboutMeView.as_view(), name='aboutme'),
    url(r'^contacts/$', ContastsView.as_view(), name='contacts'),
]
