from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #    path('', views.profile, name='users-profile'),
    path('register/', views.register, name='user-registration'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('pass-reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='pass-reset'),
]
