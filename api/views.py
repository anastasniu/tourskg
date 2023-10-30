from rest_framework import generics
from .serializers import ToursSerializer
from tours.models import Tour



class ToursList(generics.ListAPIView):

    serializer_class = ToursSerializer
    queryset = Tour.objects.all()