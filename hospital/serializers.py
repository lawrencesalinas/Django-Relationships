from rest_framework import serializers

from .models.doctor import Doctor
from .models.patient import Patient
from .models.appointment import Appointment


class PatientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Patient
    fields = '__all__'

class PatientReadSerializer(serializers.ModelSerializer):
  primary_care_physician = serializers.StringRelatedField()
  class Meta:
    model = Patient
    fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
  primary_patients = PatientSerializer(many=True, read_only=True)
  class Meta:
    model = Doctor
    fields = '__all__'

class AppointmentReadSerializer(serializers.ModelSerializer):
  doctor = DoctorSerializer()
  patient = PatientReadSerializer()
  class Meta:
    model = Appointment
    fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
  class Meta:
      model = Appointment
      fields = '__all__'