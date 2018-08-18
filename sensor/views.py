from django.shortcuts import render
from .models import Sensor, Local, Historico
from datetime import datetime, timedelta

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

def sensor(request, id):
    ago = datetime.now() - timedelta(days=30)
    sensor = Sensor.objects.get(id=id)
    media = Historico.objects.filter(sensor=sensor, time__gte=ago)
    temp = 0
    umid = 0
    luz = 0
    for i in media:
        temp += i.temperatura
        umid = i.umidade
        luz = i.luz

    temp = temp/media.count()
    umid = umid / media.count()
    luz = luz / media.count()
    historico = Historico.objects.filter(sensor=sensor)
    context = {
        'sensor': sensor,
        'historico': historico,
        'temp': temp,
        'umid': umid,
        'luz': luz,
    }
    return render(request, 'sensor/sensor.html', context)