from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'cart'
# router = DefaultRouter()
# router.register('cartitem',views.CartItemViewset)

urlpatterns = [
    # path('',include(router.urls)),
    path('listcart/',views.list_cart,name='list_cart'),
]
# urlpatterns += router.urls
