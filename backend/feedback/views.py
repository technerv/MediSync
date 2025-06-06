from rest_framework import viewsets
from .models import Feedback
from .serializers import FeedbackSerializer
from feedback.permissions import FeedbackPermission

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [FeedbackPermission,]

    def perform_create(self, serializer):
        serializer.save()