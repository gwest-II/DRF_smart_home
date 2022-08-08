from django.db import models


class SensorDetail(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)


class Measurement(models.Model):
    id_sensor = models.ForeignKey(SensorDetail, on_delete=models.CASCADE)
    temp = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
