from django.urls import path
from rest_framework import routers
from . import views
from .views import ProductViewSet

app_name = 'main'

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('menu/', views.menu, name='menu'),
    path('unlock/', views.unlocking, name='unlock'),
    path('lock/', views.locking, name='lock'),
    path('status/', views._get_status, name='status'),
    path('history/', views.History.as_view(), name='history'),
    path('product_register/', views.ProductRegister.as_view(), name='product_register'),
    path('product_register/done/', views.product_register_done, name='product_register_done'),
]
