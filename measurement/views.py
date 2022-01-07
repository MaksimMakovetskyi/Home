from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        return Response({'status': 'ОК'})


class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        return Response({'status': 'ОК'})

# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
class SensorList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAdminUser]


