from django.conf.urls import url
from core import views

urlpatterns = [
    # The home page
    url(r'^$', views.index, name='index'),
    url(r'^climate/$', views.index, name='climate'),
]