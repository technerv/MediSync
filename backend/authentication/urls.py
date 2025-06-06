from django.urls import path
from knox import views as knox_views
from .views import RegisterView, LoginView, DoctorDashboard, PatientDashboard, NurseDashboard, ReceptionistDashboard

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Register
    path('login/', LoginView.as_view(), name='login'),  # Login to get a token
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),  # Logout
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logout_all'),  # Logout all sessions
    path('doctor/dashboard', DoctorDashboard.as_view(), name='doctor-dashboard'),
    path('patient/dashboard', PatientDashboard.as_view(), name='patient-dashboard'),
    path('nurse/dashboard', NurseDashboard.as_view(), name='nurse-dashboard'),
    path('receptionist/dashboard', ReceptionistDashboard.as_view(), name='receptionist-dashboard')
]