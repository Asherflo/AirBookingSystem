from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from airlineBooking.models import Passenger
from rest_framework.decorators import api_view
from . serializers import PassengerSerializer


# Create your views here.
@api_view()
def passenger_list(request):
    query_set = Passenger.objects.all()
    serializer = PassengerSerializer(query_set, many=True)
    return Response(serializer.data)


@api_view()
def passenger_details(request, id):
    try:
        passenger = Passenger.objects.get(pk=id)
        serializer = PassengerSerializer(passenger)
        return Response(serializer.data)
    except Passenger.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

