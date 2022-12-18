from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import MyUser


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: MyUser, timestamp: int) -> str:
        return f'{user.pk}{user.password}{timestamp}{user.is_active}'

account_activation_token = AccountActivationTokenGenerator()
