from rest_framework import serializers
from .models import Drug, Prescription, PrescribedDrug, PharmacyOrder

class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'
    
class PrescribedDrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescribedDrug
        fields = '__all__'

class PharmacyOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacyOrder
        fields = '__all__'