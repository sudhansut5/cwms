# ana_web/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('App.urls')),  # Include App URLs
    path('main/', include('main.urls')),  # Include main URLs
    # Add other URL patterns as needed
]
