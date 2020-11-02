from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('menu/', views.menu, name='menu'),
    path('unlock/', views.unlocking, name='unlock'),
    path('lock/', views.locking, name='lock'),
    path('status/', views._get_status, name='status'),
    path('history/', views.History.as_view(), name='history'),
]
