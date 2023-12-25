from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .serializers import UserRegisSerializer, ChangePasswordSerializer, UsersSerializer
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
# Представление для регистрации новых пользователей


class RegistrationAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Представление для аутентификации пользователей


class CustomUserLoginView(TokenObtainPairView):
    pass
# Представление для получения списка пользователей (доступно всем)


class CustomUserList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer
# Представление для просмотра, обновления и удаления информации о пользователе


class CustomUserUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UsersSerializer
    queryset = CustomUser.objects.all()
# Представление для получения информации о текущем пользователе


class UserInfoAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UsersSerializer()

    def get(self, request, *args, **kwargs):
        current_user_serializer = UsersSerializer(request.user)
        return Response(current_user_serializer.data)
# Представление для смены пароля текущего пользователя


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']

            if not user.check_password(old_password):
                return Response({'detail': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()
            return Response({'detail': 'Password changed successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Представление для обновления токена доступа


class CustomUserTokenRefreshView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            access_token = str(token.access_token)
            return Response({'access': access_token}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'invalid token'}, status.HTTP_401_UNAUTHORIZED)
