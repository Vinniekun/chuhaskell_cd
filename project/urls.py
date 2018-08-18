"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import login, logout
from user.forms import UserAdminCreationForm
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^entrar$', login,
                      {'template_name': 'user/login.html',
                       'extra_context': {'formup': UserAdminCreationForm}
                       }, name='login'),
                  url(r'^sair$', logout, {'next_page': 'login'}, name='logout'),
                  path('', include('core.urls')),
                  path('sensores/', include('sensor.urls', namespace='sensor', )),
                  path('adm/', include('adm.urls', namespace='adm')),
                  path('user/', include('user.urls', namespace='user')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
