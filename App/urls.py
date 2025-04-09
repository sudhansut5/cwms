from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import *
from .views import PasswordResetRequestView
from django.views.decorators.cache import never_cache
from django.views.static import serve



urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.custom_login, name='custom_login'),
    path('custom_logout/', views.custom_logout, name='custom_logout'),
    path('static/<path:path>', never_cache(serve)),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password-reset/confirm/<str:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
