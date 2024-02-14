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
                return redirect('users:login')
            else:
                login(request, user)
                return redirect('index')
        else:
            messages.error(request, _('Yanlış kullanıcı adı veya şifre'))

    return render(request, 'registration/login.html')

def custom_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def custom_logout(request):
    logout(request)
    messages.success(request, _('Başarıyla Çıkış Yaptınız'))
    return redirect('users:login')


