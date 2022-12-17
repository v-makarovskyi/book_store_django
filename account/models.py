from django.db import models
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomAccountManager(BaseUserManager):
    
    def create_superuser(self, username, email, password, **additional_fields):
        
        additional_fields.setdefault('is_staff', True)
        additional_fields.setdefault('is_superuser', True)
        additional_fields.setdefault('is_active', True)

        if additional_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if additional_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(username, email, password, **additional_fields)
    
    def create_user(self, username, email, password, **additional_fields):
        if not email:
            raise ValueError(_('Вы должны преоставить действительный email'))
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **additional_fields)
        user.set_password(password)
        user.save()
    
    
class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('имя', max_length=150, unique=True)
    email = models.EmailField('email', max_length=150, unique=True)
    mobile = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
    
    def __str__(self) -> str:
        return self.username

class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('клиент'), on_delete=models.CASCADE)
    full_name = models.CharField(_('полное имя'), max_length=150)
    tel = models.CharField(_('номер телефона'), max_length=30)
    postcode = models.CharField(_('почтовый индекс'), max_length=20)
    address_line = models.CharField(_('аддресс доставки'), max_length=200)
    city = models.CharField(_('населенный пункт'), max_length=100)
    delivery_instruction = models.CharField(_('детали доставки'), max_length=255)
    created = models.DateTimeField(_('адрес создан'), auto_now_add=True)
    updated = models.DateTimeField(_('адрес обновлен'), auto_now=True)

    class Meta:
        verbose_name = 'Адрес клиента'
        verbose_name_plural = 'Адресa клиентов'
    
    def __str__(self) -> str:
        return '{} адрес'.format(self.owner)


