from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from rest_framework import generics, status
from rest_framework.response import Response

from apps.users.serializers.registration_serializers import RegistrationSerializer


class RegistrationView(generics.GenericAPIView):
   serializer_class = RegistrationSerializer

   def post(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      if serializer.is_valid():
         serializer.save(is_active=False)
         return Response(
             {
                 'message':
                 'An email has been sent to your registration please check your email and verifi your account',
             },
             status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


activation_token = PasswordResetTokenGenerator()


class ActivationAccount(generics.GenericAPIView):
   def get(self, request, *args, **kwargs):
      try:
         uid = force_text(urlsafe_base64_decode(kwargs['uid64']))
         user = get_user_model().objects.get(pk=uid)
      except:
         user = None

      if user and activation_token.check_token(user, kwargs['token']):
         user.is_active = True
         user.save()
         return Response({'message': 'Your account has been activated'}, status=status.HTTP_200_OK)
      return Response({'message': 'Your account has not been activated'}, status=status.HTTP_400_BAD_REQUEST)
