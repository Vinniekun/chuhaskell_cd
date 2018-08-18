from sensor.models import Historico, Sensor
import random
from datetime import datetime, timedelta
import time

Historico.objects.all().delete()
while True:
    ids = list(Sensor.objects.all().values("id").distinct())
    for dias in range(0,30):
        ago = datetime.now() - timedelta(days=dias)
        for i in ids:
            temp = random.randrange(0, 40)
            umi = random.randrange(0,100)
            luz = random.randrange(0,100)
            if Sensor.objects.get(id=i['id']).status:   
                h = Historico.objects.create(sensor_id=i['id'],temperatura=temp,umidade_solo=umi, umidade_ar=umi, luz=luz,time=ago)
                h.save()
    time.sleep(10)