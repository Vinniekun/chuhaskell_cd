from django.conf.urls import url
from django.urls import path
from adm import views

app_name = 'adm'
urlpatterns = [
    # The home page
    url(r'^$', views.index, name='index'),
    url(r'^usuarios$', views.usuarios, name='usuarios'),
    url(r'^user$', views.AddUser.as_view(), name='adduser'),
    path('user/<int:pk>/change/', views.UserUpdate.as_view(), name='edituser'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='deluser'),
    # path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('user/<id>/password/', views.user_change_password, name='password_user'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    url(r'^locais$', views.locais, name='locais'),
    path('local/<int:pk>/change/', views.LocalUpdate.as_view(), name='editlocal'),
    path('local/<int:pk>/delete/', views.LocalDelete.as_view(), name='deletelocal'),
    url(r'^addlocal$', views.AddLocal.as_view(), name='addlocal'),

    url(r'^sensores$', views.sensores, name='sensores'),
    path('sensor/<int:pk>/change/', views.SensorUpdate.as_view(), name='editsensor'),
    path('sensor/<int:pk>/delete/', views.SensorDelete.as_view(), name='deletesensor'),
    url(r'^addsensor$', views.AddSensor.as_view(), name='addsensor'),
]
