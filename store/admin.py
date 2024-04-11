from django.contrib import admin
from .models import Category,ImageProduct,Color,Size,Offer,Review,Product
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id','name'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'id','name','user','price','stock','is_available','created_at','updated_at','number_of_rating','avg'

@admin.register(ImageProduct)
class ImageProductAdmin(admin.ModelAdmin):
    list_display = 'id','product'

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = 'id','name'

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = 'id','name'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = 'id','user','product','rating'

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = 'id','product','discount_precentage','start_date','end_date'

