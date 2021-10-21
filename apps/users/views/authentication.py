from django.contrib.auth import get_user_model, logout

from rest_framework import generics, status
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.serializers.login_serializers import LoginSerializer


class LogIn(TokenObtainPairView):
   serializer_class = LoginSerializer


class LogOut(generics.GenericAPIView):
   serializer_class = LoginSerializer

   def post(self, request, *args, **kwargs):
      user = get_user_model().objects.filter(id=request.user.id).first()
      if user:
         RefreshToken.for_user(user=user)
         return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
      return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
