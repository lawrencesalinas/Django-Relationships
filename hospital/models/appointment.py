from django.db import models

class Appointment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    diagnosis = models.CharField(max_length=100)
    scheduled = models.DateField()
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE)

    def __str__(self):
        return self.scheduled