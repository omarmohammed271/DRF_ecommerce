from django.contrib import admin
from . models import Order,OrderProduct,OrderComplete
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
     pass

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = 'order','product','quantity','product_price','order_notes','created_at','sub_total','total'

@admin.register(OrderComplete)
class OrderCompleteAdmin(admin.ModelAdmin):
    list_display = ['order','total_price','created_at']

   

