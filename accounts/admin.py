from django.contrib import admin
from .models import Account
# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = 'first_name','last_name','username','email','date_joined','last_login'
    list_filter = 'username','email'
