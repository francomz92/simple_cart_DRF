from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail

from rest_framework.reverse import reverse

from apps.users.views.registration import activation_token


@receiver(post_save, sender=get_user_model())
def send_confirmation_email(sender, instance, created, **kwargs):
   if created:
      uid = urlsafe_base64_encode(force_bytes(instance.pk))
      token = activation_token.make_token(instance)
      domain = 'localhost:3000'
      path = reverse('users:account_activation', args=[uid, token])
      subject = 'Confirmation of account'
      message = f'Please confirm your account in this link http://{domain}{path}{uid}{token}'
      from_email = 'root@example.com'
      send_mail(subject, message, from_email, recipient_list=[instance.email])