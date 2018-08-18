from django.db import models
from time import timezone
from user.models import User

# Create your models here.
class Sensor(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    longitude = models.FloatField('Longitude')
    latitude = models.FloatField('Latitude')


class Historico(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    time = models.DateTimeField('Timestamp', default=timezone.now())
    temperatura = models.FloatField('Temperatura')
    umidade = models.FloatField('Umidade')
    luz = models.FloatField('Iluminação')



