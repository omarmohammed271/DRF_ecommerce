from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('category',views.CategoryVIew)
router.register('product',views.ProductView)
router.register('imageproduct',views.ImageProductView)
router.register('size',views.SizeView)
router.register('color',views.ColorView)
router.register('offer',views.OfferView)
router.register('review',views.ReviewView)

app_name='store'
urlpatterns = [
    # path('',include(router.urls)),
    path('product/<str:id>/<str:slug>/', views.ProductView.as_view({'get': 'slug_product'}), name='slug_product'),
    path('product/search_by_category/<str:id>/', views.ProductView.as_view({'get': 'search_by_category'}), name='search_by_category'),
    
]
urlpatterns += router.urls


