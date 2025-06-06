from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import login
from .serializers import RegisterSerializer
from knox.models import AuthToken
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .permissions import IsDoctor, IsNurse, IsPatient, IsReceptionist

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request, user)  # Auto-login after registration
        token = AuthToken.objects.create(user)[1]  # Generate Knox token
        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            "token": token
        })

class LoginView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token = AuthToken.objects.create(user)[1]  # Create Knox token
        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            "token": token
        })

class DoctorDashboard(APIView):
    permission_classes = [IsDoctor]

    def get(self, request):
        return Response({"message": "Welcome, Doctor!"})

class PatientDashboard(APIView):
    permission_classes = [IsPatient]

    def get(self, request):
        return Response({"message": "Welcome, Patient!"})

class NurseDashboard(APIView):
    permission_classes = [IsNurse]

    def get(self, request):
        return Response({"message": "Welcome, Nurse"})

class ReceptionistDashboard(APIView):
    permission_classes = [IsReceptionist]

    def get(self, request):
        return Response({"message": "Welcome, Receptionist!"})


# from django.contrib.auth import get_user_model
# from rest_framework.views import APIView
# from rest_framework import generics, permissions, status
# from rest_framework.response import Response
# from .serializers import UserSerializer, RegisterSerializer

# User = get_user_model()

# # class RegisterView(APIView):
# #     def post(self, request):
# #         username = request.data.get('username')
# #         password = request.data.get('password')
# #         if not username or not password:
# #             return Response({'error': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)
# #         user = User.objects.create_user(username=username, password=password)
# #         return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    
# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer
#     permission_classes = [permissions.AllowAny]

# class LoginView(generics.GenericAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         })

# class UserView(generics.RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_object(self):
#         return self.request.user