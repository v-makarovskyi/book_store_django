from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.urls import reverse

from .models import MyUser, Address
from .forms import RegistrationForm, UserEditForm
from .tokens import account_activation_token

def account_register(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')

    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.email = register_form.cleaned_data['email']
            user.set_password(register_form.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Активация учетной записи'
            message = render_to_string('account/registration/account_activation_email.html',
                {
                    'user': user,
                    'domain': current_site,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user)
                }
            )
            user.email_user(subject=subject, message=message)
            return render(request, 'account/registration/register_email_confirm.html', {'form': register_form})
        else:
            return render(request, 'account/registration/register.html', {'form': register_form})
    else:
        register_form = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form': register_form})
    

def account_activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = MyUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExists):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')


@login_required
def dashboard(request):
    return render(request, 'account/dashboard/dashboard.html', {})

@login_required
def edit_details(request):
    instance = request.user
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=instance)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=instance)
    return render(request, 'account/dashboard/edit_details.html', {'user_form': user_form})

@login_required
def delete_user(request):
    user = MyUser.objects.get(username=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('account:delete_confirmation')


@login_required
def view_address(request):
    addresses = Address.objects.filter(owner=request.user)
    return render(request, 'account/dashboard/addresses.html', {'addresses': addresses})
