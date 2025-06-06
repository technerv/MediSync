from rest_framework import serializers
from .models import ElectronicHealthRecord

class ElectronicHealthRecordSerializer(serializers.ModelSerializer):

    date_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    patient = serializers.CharField()
    doctor = serializers.CharField()

    class Meta:
        model = ElectronicHealthRecord
        # fields = '__all__'  # or specify the fields you want to include
        fields = ['id', 'patient', 'doctor', 'notes', 'allergies', 'medical_history', 'vital_signs', 'date_created' ]

# class ElectronicHealthRecordDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ElectronicHealthRecord
#         fields = ['id', 'patient', 'doctor', 'date', 'notes', 'prescriptions', 'diagnosis']  # specify fields as needed