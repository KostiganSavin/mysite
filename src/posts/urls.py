from django.conf.urls import url
from .views import IndexView, PostsListView


urlpatterns =[
    # url(r'^$', IndexView.as_view(), name='posts_list'),
    url(r'^$', PostsListView.as_view(), name='posts_list'),
]
