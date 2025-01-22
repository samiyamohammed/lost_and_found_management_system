from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer, RegisterSerializer
from .rabbitmq_utils import publish_message 
from rest_framework.permissions import AllowAny

class AssignRoleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        email = request.data.get('email')
        role = request.data.get('role')

        if role not in ['user', 'admin']:  # Validate role
            return Response({"error": "Invalid role"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            user.role = role
            user.is_staff = role == 'admin'
            user.is_superuser = role == 'admin'
            user.save()

            # Publish a message to RabbitMQ
            message = {
                "event": "assign_role",
                "email": email,
                "role": role,
            }
            publish_message("user_events", str(message))

            return Response({"message": "Role assigned successfully"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class CreateAdminUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Only allow superusers to create admin users
        if not request.user.is_superuser:
            return Response({"error": "You are not authorized to create admin users."}, status=status.HTTP_403_FORBIDDEN)

        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_staff = True
            user.is_superuser = True
            user.role = "admin"  # Explicitly set the role to "admin"
            user.save()

            # Publish a message to RabbitMQ
            message = {
                "event": "create_admin",
                "admin_email": user.email,
            }
            publish_message("user_events", str(message))

            return Response({
                "message": "Admin user created successfully",
                "data": UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Publish a message to RabbitMQ
            message = {
                "event": "register_user",
                "user_id": user.id,
                "email": user.email,
            }
            publish_message("user_events", str(message))

            return Response({
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "message": "User created successfully"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                raise ValueError("Invalid credentials")
            refresh = RefreshToken.for_user(user)

            # Publish a message to RabbitMQ
            message = {
                "event": "login",
                "user_id": user.id,
                "email": user.email,
            }
            publish_message("user_events", str(message))

            return Response({
                "status": "success",
                "message": "Login successful",
                "user_id": str(user.id),
                "token": str(refresh.access_token)
            }, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# class UserProfileView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, user_id):
#         try:
#             user = User.objects.get(id=user_id)
#             serializer = UserSerializer(user)

#             # Publish a message to RabbitMQ
#             message = {
#                 "event": "view_profile",
#                 "user_id": user.id,
#                 "email": user.email,
#             }
#             publish_message("user_events", str(message))

#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except User.DoesNotExist:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
from rest_framework.permissions import AllowAny

class UserProfileView(APIView):
    permission_classes = [AllowAny]  # Make the view accessible without authentication

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user)

            # Publish a message to RabbitMQ
            message = {
                "event": "view_profile",
                "user_id": user.id,
                "email": user.email,
            }
            publish_message("user_events", str(message))

            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
