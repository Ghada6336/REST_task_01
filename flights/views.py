from .models import Flight, Booking
from django.shortcuts import render
from datetime import datetime 
from rest_framework.generics import ListAPIView
from .serializers import FlightSerializer, BookingSerializer

class FlightList(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class BookingList(ListAPIView):
    queryset = Booking.objects.filter(date__gt=datetime.today())
    serializer_class = BookingSerializer
