from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('login/',views.login_view,name='login_view'),
    path('register/',views.register,name='register'),
    path('reset_password/',views.reset_password,name='reset_password'),
    path('new_password/',views.new_password,name='new_password'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
]
