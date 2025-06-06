from rest_framework import serializers
from .models import TelemedicineSession, TelemedicineFeedback

class TelemedicineSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelemedicineSession
        fields = '__all__'

class TelemedicineFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelemedicineFeedback
        fields = '__all__'