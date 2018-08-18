from sensor.models import Historico, Sensor
import random
from datetime import datetime, timedelta

while True:
    ids = list(Sensor.objects.all().values("id").distinct())
    for dias in range(0,30):
        ago = datetime.now() - timedelta(days=dias)
        for i in ids:
            print(i.values())
            temp = random.randrange(0, 40)
            umi = random.randrange(0,100)
            luz = random.randrange(0,100)
            if Sensor.objects.get(id=i['id']).status:   
                h = Historico.objects.create(sensor_id=i['id'],temperatura=temp,umidade=umi,luz=luz,time=ago)
                h.save()
    sleep(10)