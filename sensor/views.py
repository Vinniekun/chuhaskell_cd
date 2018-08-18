from django.shortcuts import render
from .models import Sensor, Local


# Create your views here.
def list(request):
    locais = Local.objects.filter(usuario=request.user)

    context = {
        'sensores': Sensor.objects.filter(local__usuario=request.user),
    }
    return render(request, 'sensor/list.html', context)
