from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.openweather.api_requests import *
from sensor.models import *
from random import randint
from datetime import datetime, timedelta
import math

# Create your views here.
@login_required
def index(request):
    #dados da primeira cidade
    _locals = Local.objects.filter(usuario=request.user.id)
    local = _locals.first()
    forecast = None
    if local:
        forecast = get_day_forecast(local.coord_NW_lat, local.coord_NW_lat)
    
    #grafico
    consumoDia = [[i, randint(100, 200)] for i in range(20)]
    print(consumoDia)
    return render(request, 'core/index.html', {'consumoDia':consumoDia, 'local':local, 'forecast':forecast})

@login_required
def climate(request):
    local_objs = Local.objects.filter(usuario=request.user.id)
    opened_places = []
    locais = []
    weekday = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    for local in local_objs:
        lat, lon = local.coord_NW_lat, local.coord_NW_lat
        city, state = local.cidade, local.estado
        if [city, state] in opened_places:
            continue
        opened_places.append([city, state])
        local_data = {'cidade':city, 'estado':state, 'hora': datetime.now().strftime('%H:%M'), 'forecast':[]}
        forecast = get_5days_forecast(lat, lon)
        for i, day in enumerate(forecast['list'][::8]):
            dt = datetime.fromtimestamp(day['dt'])
            day_data = {
                'temperatura': day['main']['temp'],
                'descricao': day['weather'][0]['description'],
                'vento': day['wind']['speed'],
                'icone': get_icon_name(day['weather'][0]['id']),
                'dia': weekday[dt.weekday()]
            }
            if i > 0:
                day_data['temperatura'] = int (day_data['temperatura'])
                day_data['dia'] = day_data['dia'][:3]
            local_data['forecast'].append(day_data)
        locais.append(local_data)

    return render(request, 'core/climate.html', {'locais': locais})

def distance_between_coords(lat1, lon1, lat2, lon2):
    R = 6371 #metros
    delta_lat = abs(lat2-lat1)
    delta_lon = abs(lon2-lon1)

    a = math.sin(delta_lat/2) * math.sin(delta_lat/2) + \
        math.cos(lat1) * math.cos(lat2) * \
        math.sin(delta_lon/2) * math.sin(delta_lon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c

@login_required
def graphs(request):
    local_objs = Local.objects.filter(usuario=request.user.id)
    id = request.GET.get('id') or local_objs[0].id

    local_items = list(local_objs.values_list('nome','id'))
    local = Local.objects.filter(usuario=request.user.id, id=id)[0]
    date_past = datetime.now().date() - timedelta(days=30)
    hist_objs = Historico.objects

    graph_data = {
        'nome' : local.nome,
        'cidade': local.cidade,
        'estado': local.estado,
        'area': "{:.2f}".format(distance_between_coords(
            local.coord_NW_lat, local.coord_NW_long,
            local.coord_NW_lat, local.coord_SE_long
        ) * distance_between_coords(
            local.coord_NW_lat, local.coord_SE_long,
            local.coord_SE_lat, local.coord_SE_long
        )),
        'sensores': [],
        'idade': (datetime.now(hist_objs.all()[0].time.tzinfo) - hist_objs.all()[0].time).days
    }
    sensores = Sensor.objects.filter(local=local.id)
    for sensor in sensores:
        sensor_data = {
            'id': sensor.id
        }
        sensor_data['temp'] = list(hist_objs.filter(time__gte=date_past).values_list('time', 'temperatura'))
        sensor_data['umi_solo'] = list(hist_objs.filter(time__gte=date_past).values_list('time', 'umidade_solo'))
        sensor_data['umi_ar'] = list(hist_objs.filter(time__gte=date_past).values_list('time', 'umidade_ar'))
        for n in ['temp', 'umi_solo', 'umi_ar']:
            for i in range(len(sensor_data[n])):
                sensor_data[n][i] = [sensor_data[n][i][0].strftime('%m/%d-%H:%M'), sensor_data[n][i][1]]
        graph_data['sensores'].append(sensor_data)

    return render(request, 'core/graphs.html', {'local_items': local_items, 'local': graph_data})

