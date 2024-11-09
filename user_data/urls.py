from django.urls import path
from . import views

urlpatterns = [
    path('', views.save_name, name='save_name'),
]
