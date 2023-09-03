from django.urls import path
from . import views

app_name = 'StaffApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('rules/', views.rules, name='rules'),
    path('staff/', views.staff, name='staff'),
    path('online-tables/', views.online_tables, name='online-tables'),
    path('add_member/', views.add_member, name='add_member'),
    path('delete_staff/<int:staff_id>/', views.delete_staff, name='delete_staff'),
    path('staff/<str:staff_name>/', views.staff_details, name='staff_details'),
    path('edit_member/<int:id>', views.edit_member, name='edit_member'),

    path('registrate/', views.registrate, name='registrate'),
    path('login/', views.ajax_login, name='ajax_login'),
]