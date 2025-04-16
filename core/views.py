from rest_framework import viewsets
from .models import Crop, WeatherInfo
from .serializers import MyCropSerializer
from .serializers import WeatherInfoSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Smart Agri Platform!")


class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = MyCropSerializer

class WeatherInfoViewSet(viewsets.ModelViewSet):
    queryset = WeatherInfo.objects.all()
    serializer_class = WeatherInfoSerializer
    # Create your views here.
