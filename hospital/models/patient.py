from django.db import models
from .doctor import Doctor
from .appointment import Appointment

class Patient(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  diagnosis = models.CharField(max_length=200)
  born_on = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


  primary_care_physician = models.ForeignKey(Doctor, related_name='primary_patients', on_delete=models.CASCADE)
  appointment_doctors = models.ManyToManyField(
    Doctor,
    through=Appointment,
    through_fields=('patient', 'doctor')
    )

  def __str__(self):
    return f"{self.first_name} {self.last_name}"
