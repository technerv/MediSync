from rest_framework import serializers
from .models import Patient, NextOfKin, Appointment, Triage, Consultation, Prescription, PrescribedDrug, Referral

class PatientSerializer(serializers.ModelSerializer):

    insurance = serializers.StringRelatedField()

    class Meta:
        model = Patient
        fields = ['id','first_name','second_name','gender','date_of_birth','phone','email','insurance']
        # fields = '__all__'

class NextOfKinSerializer(serializers.ModelSerializer):

    patient_id = serializers.StringRelatedField()

    class Meta:
        model = NextOfKin
        # fields = '__all__'
        fields = ['patient_id', 'first_name', 'second_name', 'relationship', 'tel_no', 'email_address', 'residence']

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class TriageSerializer(serializers.ModelSerializer):

    patient_id = serializers.StringRelatedField()
    date_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    
    class Meta:
        model = Triage
        # fields = '__all__'
        fields = ['id', 'patient_id', 'created_by', 'date_created', 'temperature', 'height', 'weight', 'pulse', 'fee', 'notes']

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class PrescribedDrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescribedDrug
        fields = '__all__'

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = '__all__'