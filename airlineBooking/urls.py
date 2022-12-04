from django.urls import path
from . import views

urlpatterns = [
    path('passenger/', views.passenger_list),
    path('passenger/<int:id>/', views.passenger_details),


]
