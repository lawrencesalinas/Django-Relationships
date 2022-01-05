from rest_framework import serializers

from .models.doctor import Doctor
from .models.patient import Patient


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

class DoctorReadSerializer(serializers.ModelSerializer):
  primary_patients = serializers.StringRelatedField()
  class Meta:
    model = Doctor
    fields = '__all__'
