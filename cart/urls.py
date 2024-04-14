from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'cart'
router = DefaultRouter()
router.register('cartitem',views.CartItemViewset)

urlpatterns = [
    
]
urlpatterns += router.urls
