from django.shortcuts import render
from .models import Sensor, Local


# Create your views here.
def sensores(request):
    sensores = []

    locais = Local.objects.filter(usuario=request.user).values_list('nome')
    for local in locais:
        sensores.append({'nome': local[0], 'sensores': list(Sensor.objects.filter(local__nome=local[0]).values_list('id', 'longitude', 'latitude'))})
    context = {
        'locais': sensores,
    }
    return render(request, 'sensor/list.html', context)
