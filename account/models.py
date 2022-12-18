from django.db import models

import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email, EmailValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _


class MyUserManager(BaseUserManager):
    def validate__email(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('Вы должны ввести действительный email'))

    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        if email:
            email = self.normalize_email(email)
            self.validate__email(email)
        else:
            raise ValueError(
                _('Аккаунт суперпользователя: Вы должны предоставить действительный адрес электронной почты'))
        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password, **other_fields):
        if email:
            email = self.normalize_email(email)
            self.validate__email(email)
        else:
            raise ValueError(
                _('Аллаунт пользователя: Вы должны предоставить действительный адрес электронной почты'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email_validator = EmailValidator()
    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(_('электронная почта'), unique=True, validators=[
        email_validator], error_messages={
        'обязательное поле': _('Вы должны предоставить действительный адрес электронной почты.')})
    username = models.CharField(_('имя'), max_length=150, help_text=_(
        'Введите имя. Не более 150 символов'), validators=[username_validator])
    phone = models.CharField(_('номер телефона'), max_length=20, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('Профиль пользователя')
        verbose_name_plural = _('Профили пользователей')
    
    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'test@test.pl',
            [self.email],
            fail_silently=False
        )

    def __str__(self) -> str:
        return self.username


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(MyUser, verbose_name=_('клиент'), on_delete=models.CASCADE)
    full_name = models.CharField(_('полное имя'), max_length=200)
    phone = models.CharField(_('номер телефона'), max_length=20)
    postcode = models.CharField(_('почтовый индекс'), max_length=6)
    address_line = models.CharField(_('адрес'), max_length=150)
    town_city = models.CharField(_('область/район/населенный пункт'), max_length=150)
    delivery_instruction = models.CharField(_('детали(доставка)'), max_length=255)
    created = models.DateTimeField(_('адрес добавлен'), auto_now_add=True)
    updated = models.DateTimeField(_('адрес обновлен'), auto_now=True)
    default = models.BooleanField(_('адрес по умолчанию'), default=False)

    class Meta:
        verbose_name = 'Адрес пользователя'
        verbose_name_plural = 'Адреса пользователя'
    
    def __str__(self) -> str:
        return '{} адрес'.format(self.full_name)
