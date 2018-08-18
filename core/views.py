from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.openweather.api_requests import *
from models import *
from random import randint
from datetime import datetime

# Create your views here.
@login_required
def index(request):
    consumoDia = [[i, randint(100, 200)] for i in range(20)]
    print(consumoDia)
    return render(request, 'core/index.html', {'consumoDia':consumoDia})

@login_required
def climate(request):
    _locals = Local.objects.filter(usuario=request.user.id) # user_id?
    #TODO: consultas à api do openwheatermap
    opened_places = []
    weekday = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    locais = []
    for local in _locals:
        lat, lon = local.coord_NW_lat, local.coord_NW_lat
        city, state = local.cidade, local.estado
        if [city, state] in opened_places:
            continue
        else:
        opened_places.append([city, state])
        dic_for = {'cidade':city, 'estado':state, 'forecast':[]}
        forecast = get_7days_forecast(lat, lon)
        for i, day in enumerate(forecast['list'][::8]):
            dt = datetime.fromtimestamp(day['dt'])
            day_data = {
                'temperatura': day['main']['temp'] if i == 0 else int(day['main']['temp']),
                'descricao': day['weather'][0]['description'],
                'icone': get_icon_name(day['weather'][0]['id']),
                'dia': weekday[dt.weekday()] if i == 0 else weekday[dt.weekday()][:3],
                'hora': datetime.now().strftime('%H:%M')
            }
            dic_for['forecast'].append(day_data)
        locais.append(dic_for)

    return render(request, 'core/climate.html', {'locais': locais})