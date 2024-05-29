from django.contrib import admin
from django.urls import path, include
from inventory.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
    path('api/', api.urls),
]
