from .models import Tour
from api.serializers import ToursSerializer
from rest_framework import generics


class TourAPIView(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = ToursSerializer
