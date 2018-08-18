from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from random import randint

# Create your views here.
@login_required
def index(request):
    consumoDia = [[i, randint(100, 200)] for i in range(20)]
    print(consumoDia)
    return render(request, 'core/index.html', {'consumoDia':consumoDia})

@login_required
def climate(request):
    
    return render(request, 'core/climate.html')