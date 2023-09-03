from django.urls import path
from . import views

app_name = 'StudentApp'

urlpatterns = [
    path('', views.index, name='index'),
]