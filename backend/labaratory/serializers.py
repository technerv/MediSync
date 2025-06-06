from rest_framework import serializers
from .models import LaboratoryTest, LaboratoryResult, Sample

class LaboratoryTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratoryTest
        fields = '__all__'

class LaboratoryResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratoryResult
        fields = '__all__'

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = '_all_'