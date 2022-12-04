from django.db import models


# Create your models here.


class Passenger(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phoneNumber = models.IntegerField()
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=45)
    password = models.TextField()


class Booking(models.Model):
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


class Ticket(models.Model):
    TICKET_ECONOMIC = 'E'
    TICKET_BUSINESS = 'B'
    TICKET_FIRST_CLASS = 'F'

    TICKET_CHOICE = [
        (TICKET_ECONOMIC, 'Economic'),
        (TICKET_BUSINESS, 'Business'),
        (TICKET_FIRST_CLASS, 'First_class')
    ]
    ticket_type = models.CharField(max_length=1, choices=TICKET_CHOICE, default=TICKET_BUSINESS)
    ticket_booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    ticket_date = models.DateField(auto_now_add=True)
    ticket_description = models.CharField(max_length=255)
#
 #
# class Address(models.Model):
#     # zip = models.PositiveIntegerField()
#     street = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
