from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.appointment import Appointment
from ..serializers import AppointmentSerializer, AppointmentReadSerializer

# Create your views here.
class Appointments(APIView):
    def get(self, request):
        """Index Request"""
        appointment = Appointment.objects.all()[:10]
        data = AppointmentReadSerializer(appointment, many=True).data
        return Response(data)

    serializer_class = AppointmentSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        appointment = AppointmentSerializer(data=request.data)
        if appointment.is_valid():
            b = appointment.save()
            return Response(appointment.data, status=status.HTTP_201_CREATED)
        else:
            return Response(appointment.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        appointment = get_object_or_404(Appointment, pk=pk)
        data = AppointmentReadSerializer(appointment).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        appointment = get_object_or_404(Appointment, pk=pk)
        ms = AppointmentSerializer(appointment, data=request.data)
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        appointment = get_object_or_404(Appointment, pk=pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)