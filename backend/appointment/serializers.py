from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):

    appointment_date_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    patient = serializers.CharField()
    assigned_doctor = serializers.CharField()

    class Meta:
        model = Appointment
        fields = ['id', 'appointment_date_time', 'patient', 'assigned_doctor', 'status', 'reason', 'fee']