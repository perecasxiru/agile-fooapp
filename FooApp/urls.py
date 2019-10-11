
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('products/', views.products, name='products'),
    path('products/<str:prod_id>', views.product, name='product'),
    path('products/<str:prod_id>/edit', views.product_edit, name='product_edit'),
    path('product_create', views.product_create, name='product_create'),
    path('product_delete/<str:prod_id>', views.product_delete, name='product_delete')
]
