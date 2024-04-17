from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'order'

router = DefaultRouter()
# router.register('order',views.OrderView)
# router.register('orderproduct',views.OrderProductView)

urlpatterns = [
    path('make_order/',views.make_order,name='make_order'),
    path('place_order/',views.place_order,name='place_order'),
    path('order_complete/',views.order_complete,name='order_complete'),
]
urlpatterns += router.urls

