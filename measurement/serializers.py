from rest_framework import serializers
from .models import SensorDetail, Measurement


class SensorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorDetail
        fields = ['id', 'name', 'description']
# TODO: опишите необходимые сериализаторы


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id_sensor', 'temp', 'date']
