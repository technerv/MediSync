from rest_framework import serializers
from .models import RadiologyReport, RadiologyTest

class RadiologyTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyTest
        fields = '__all__'

class RadiologyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyReport
        fields = '__all__'