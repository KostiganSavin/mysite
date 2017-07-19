from django.conf.urls import url
from .views import ContactsView

urlpatterns =[
    url(r'^$',ContactsView.as_view(), name='contacts')
]
