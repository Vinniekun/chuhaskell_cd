from django.db import models
from time import timezone
from user.models import User


class Local(models.Model):
    pais = models.CharField('País', max_length=50)
    estado = models.CharField('Estado', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    nome = models.CharField('Nome de Identificação', max_length=50, unique=True)
    
    def locais(self, filename):
        return 'locais/' + str(self.empresa) + '.' + filename.split('.')[-1]

    dir_imagem = models.ImageField('Imagem', upload_to=locais, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    coord_NW_long = models.FloatField('Coordenada NW long')
    coord_NW_lat = models.FloatField('Coordenada NW lat')
    coord_SE_long = models.FloatField('Coordenada SE long')
    coord_SE_lat = models.FloatField('Coordenada SE lat')

    def __str__(self):
        return self.pais + '/' + self.estado + '/' + self.cidade + '/' + self.nome


class Sensor(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    longitude = models.FloatField('Longitude')
    latitude = models.FloatField('Latitude')

    def __str__(self):
        return self.local.nome + '/' + str(self.id)


class Historico(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    time = models.DateTimeField('Timestamp', auto_now_add=True)
    temperatura = models.FloatField('Temperatura')
    umidade = models.FloatField('Umidade')
    luz = models.FloatField('Iluminação')

    def __str__(self):
        return self.sensor
