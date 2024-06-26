
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('admin/', admin.site.urls),
    path('api/store/',include('store.urls',namespace='store')),
    path('api/cart/',include('cart.urls',namespace='cart')),
    path('api/order/',include('order.urls',namespace='order')),
    path('api/contact/',include('contact.urls',namespace='contact')),
    path('tokenrequest/',obtain_auth_token),
    
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
