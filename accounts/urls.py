from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import custom_login, custom_logout, custom_register

app_name = 'accounts'

urlpatterns = [
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('register/', custom_register, name='register'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset_form.html'), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    
]