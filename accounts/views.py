from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
# Create your views here.

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_seller:
                messages.error(request, _('Böyle Bir Kullanıcı Bulunamadı'))
                return redirect('accounts:login')
            else:
                login(request, user)
                return redirect('index')
        else:
            messages.error(request, _('Invalid email or password. Please try again.'))

    return render(request, 'accounts/login.html')

def custom_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your account has been created! You can login now.'))
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def custom_logout(request):
    logout(request)
    messages.success(request, _('You have been logged out successfully.'))
    return redirect('accounts:login')


