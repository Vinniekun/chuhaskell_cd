from django.conf.urls import url
from sensor import views
from django.urls import path

app_name = 'sensor'

urlpatterns = [
    # The home page
    path('list', views.sensores, name='list'),
    path('<int:id>', views.sensor, name='sensor'),
]
