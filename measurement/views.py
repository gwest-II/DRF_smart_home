# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .serializers import SensorDetailSerializer, MeasurementSerializer
from measurement.models import SensorDetail, Measurement


class SensorList(ListAPIView):
    queryset = SensorDetail.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        serializer = SensorDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorView(RetrieveAPIView):
    queryset = SensorDetail.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sensor = self.get_object()
        serializer = SensorDetailSerializer(sensor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeasurementList(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

