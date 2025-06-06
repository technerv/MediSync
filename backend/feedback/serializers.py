from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):

    user = serializers.CharField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Feedback
        # fields = '__all__'
        fields = ['user', 'feedback_text', 'created_at']