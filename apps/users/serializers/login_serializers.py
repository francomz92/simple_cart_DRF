from datetime import datetime
from django.contrib.sessions.models import Session
from django.contrib.auth import login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .user_serializers import UserSerializer


class LoginSerializer(TokenObtainPairSerializer):
   def validate(self, attrs):
      data = super().validate(attrs)
      data['user'] = UserSerializer(self.user).data
      data['message'] = 'Login successful'

      request = self.context.get('request')
      login(request=request, user=self.user)

      # sessions = Session.objects.filter(expire_date__gte=datetime.now())
      # if sessions.exists():
      #    for session in sessions:
      #       session_data = session.get_decoded()
      #       if session_data and self.user.id == int(session_data.get('_auth_user_id')):
      #          sessions.delete()

      return data