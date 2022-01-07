from django.contrib import admin
from django.urls import path

from measurement.views import SensorView, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor/', SensorView.as_view()),
    path('measurement/', MeasurementView.as_view()),
]
