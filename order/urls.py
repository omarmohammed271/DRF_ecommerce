from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'order'

router = DefaultRouter()
router.register('order',views.OrderView)
router.register('orderproduct',views.OrderProductView)

urlpatterns = [
    
]
urlpatterns += router.urls

