from rest_framework import serializers
from .models import Doctor, DoctorAvailability

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'  # or specify the fields you want to include, e.g., ['id', 'first_name', 'last_name', 'specialization']

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    doctor = serializers.StringRelatedField()
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()

    class Meta:
        model = DoctorAvailability
        fields = ['doctor','day_of_week','start_time','end_time']