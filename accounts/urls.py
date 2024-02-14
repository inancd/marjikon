from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import custom_login, custom_logout, custom_register

app_name = 'accounts'

urlpatterns = [
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('register/', custom_register, name='register'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done'), template_name='registration/password_reset_form.html'),
         name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
