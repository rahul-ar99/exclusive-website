from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('',views.index, name='index'),
    path('product',views.view_products, name='view_products'),
    path('productlist', views.products_list, name='product_list'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('product/<int:id>/', views.product, name='product' ),
    path('add-product-page',views.add_product_page,name='add-product-page'),
    path('add_product',views.add_product,name='add_product')
]
