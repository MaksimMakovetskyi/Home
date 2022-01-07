from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


class Measurement(models.Model):
    sensorID = models.ForeignKey(Sensor, on_delete=models.CASCADE,)
    temperature = models.IntegerField()
    date = models.DateField(auto_now_add=True)


