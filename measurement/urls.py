from django.urls import path
from measurement.views import SensorList, SensorView, MeasurementList
urlpatterns = [
    path('sensors/', SensorList.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementList.as_view())

    # TODO: зарегистрируйте необходимые маршруты
]
