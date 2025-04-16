from rest_framework import serializers
from .models import Crop, WeatherInfo


class MyCropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'


class WeatherInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherInfo
        fields = '__all__'

