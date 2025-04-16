from django.urls import path, include
from .views import home
from rest_framework.routers import DefaultRouter
from .views import CropViewSet, WeatherInfoViewSet


router = DefaultRouter()
router.register(r'crops', CropViewSet)
router.register(r'weather', WeatherInfoViewSet)


urlpatterns = [
    path('',home),
    path('', include(router.urls)),
]
