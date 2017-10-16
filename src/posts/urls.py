from django.conf.urls import url
from .views import IndexView, PostsListView, PostDetailView


urlpatterns =[
    # url(r'^$', IndexView.as_view(), name='posts_list'),
    url(r"^$", PostsListView.as_view(), name="posts_list"),
    url(r"^(?P<pk>\d+)/$", PostDetailView.as_view(), name = "post_detail"), 
]
