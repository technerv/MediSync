from django.contrib import admin
from .models import Feedback

# admin.site.register(Feedback)
@admin.register(Feedback)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'feedback_text', 'created_at')