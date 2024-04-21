from django.urls import path
from . import views


app_name = 'contact'
urlpatterns = [
    
    path('',views.contact,name='contact'),
    path('mail/',views.mail_us,name='mail_us'),
    
]