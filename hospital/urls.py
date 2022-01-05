from django.urls import path


from hospital.views.appointment_views import Appointments, AppointmentDetail

from .views.patient_views import Patients, PatientDetail
from .views.doctor_views import Doctors, DoctorDetail

urlpatterns = [
    path('doctors', Doctors.as_view(), name='doctors'),
    path('doctors/<int:pk>', DoctorDetail.as_view(), name='author_detail'),
    path('patients', Patients.as_view(), name='patients'),
    path('patients/<int:pk>', PatientDetail.as_view(), name='patient_detail'),
    path('appointment', Appointments.as_view(), name='appointment'),
    path('loans/<int:pk>', AppointmentDetail.as_view(), name='appointment_detail'),
]
