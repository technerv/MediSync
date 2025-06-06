from django.contrib import admin
from .models import TelemedicineSession, TelemedicineFeedback

@admin.register(TelemedicineSession)
class TelemedicineSessionModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'session_date_time', 'status', 'notes', 'created_at', 'updated_at')

@admin.register(TelemedicineFeedback)
class TelemedicineFeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('session', 'patient', 'rating', 'comments', 'created_at')