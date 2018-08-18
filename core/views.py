from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.openweather.api_requests import *
from sensor.models import *
from random import randint
from datetime import datetime

# Create your views here.
@login_required
def index(request):
    #dados da primeira cidade
    _locals = Local.objects.filter(usuario=request.user.id)
    local = _locals[0]
    forecast = get_day_forecast(local.coord_NW_lat, local.coord_NW_lat)
    
    #grafico
    consumoDia = [[i, randint(100, 200)] for i in range(20)]
    print(consumoDia)
    return render(request, 'core/index.html', {'consumoDia':consumoDia, 'local':local, 'forecast':forecast})

@login_required
def climate(request):
    _locals = Local.objects.filter(usuario=request.user.id)
    opened_places = []
    weekday = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    locais = []
    for local in _locals:
        lat, lon = local.coord_NW_lat, local.coord_NW_lat
        city, state = local.cidade, local.estado
        if [city, state] in opened_places:
            continue
        opened_places.append([city, state])
        dic_for = {'cidade':city, 'estado':state, 'hora': datetime.now().strftime('%H:%M'), 'forecast':[]}
        forecast = get_7days_forecast(lat, lon)
        for i, day in enumerate(forecast['list'][::8]):
            dt = datetime.fromtimestamp(day['dt'])
            day_data = {
                'temperatura': day['main']['temp'] if i == 0 else int(day['main']['temp']),
                'descricao': day['weather'][0]['description'],
                'vento': day['wind']['speed'],
                'icone': get_icon_name(day['weather'][0]['id']),
                'dia': weekday[dt.weekday()] if i == 0 else weekday[dt.weekday()][:3],
            }
            dic_for['forecast'].append(day_data)
        locais.append(dic_for)

    return render(request, 'core/climate.html', {'locais': locais})