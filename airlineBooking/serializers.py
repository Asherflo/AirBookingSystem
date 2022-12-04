from abc import ABC

from rest_framework import serializers

from airlineBooking.models import Passenger


class PassengerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    phoneNumber = serializers.IntegerField()
    email = serializers.EmailField(max_length=254)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(max_length=13)


class BookingSerializer(serializers.Serializer):
    BOOKING_FIRST_CLASS = 'F'
    BOOKING_BUSINESS = 'B'
    BOOKING_ECONOMIC = 'C'

    BOOKING_CHOICE = [
        (BOOKING_FIRST_CLASS, 'First_class'),
        (BOOKING_BUSINESS, 'Business'),
        (BOOKING_ECONOMIC, 'Economic'),
    ]
    booking_type = models.CharField(max_length=1, choices=BOOKING_CHOICE, default=BOOKING_BUSINESS)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    booking_description = models.TextField()
