from django.urls import path
from .views import url_list

urlpatterns = [
    path('', url_list, name='url_list'),
]
