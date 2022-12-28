from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm

from .models import MyUser


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        label='Введите имя', max_length=50, help_text='* обязательное поле',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'usernameInput', }))
    email = forms.CharField(label='Ваш email', max_length=150, help_text='* обязательное поле',
                            error_messages={
                                'обязательно': 'Вы не предоставили email'},
                            widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailInput'}))
    password = forms.CharField(label='Введите пароль', min_length=5,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'passwordlInput'}))
    password1 = forms.CharField(label='Повторите пароль', min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'passwordConfirmInput'}))

    class Meta:
        model = MyUser
        fields = ['username', 'email']

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = MyUser.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError(
                'Пользователь с таким именем уже существует')
        return username

    def check_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

    def check_email(self):
        email = self.cleaned_data['email']
        if MyUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Вы не можете войти на сайт с этим email. Попробуйте ввести другой')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Введите email', max_length=150,
                               error_messages={
                                   'обязательно': 'Вы не предоставили email'},
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Введите пароль', min_length=5,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите email', }))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = MyUser.objects.filter(email=email)
        if not u:
            raise forms.ValidationError('Email не найден')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'newpass1'}))
    new_password2 = forms.CharField(label='Повторите новый пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'newpass2'}))


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label='Электронная почта аккаунта (не может быть изменена)', max_length=200, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'emailInput', 'readonly': 'readonly'}))
    username = forms.CharField(label='имя пользователя', max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите имя', 'id': 'usernameInput'}))
    phone = forms.CharField(label='Номер телефона', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'номер телефона', 'id': 'phoneInput'}))

    class Meta:
        model = MyUser
        fields = ['email', 'username', 'phone']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['username'].required = True