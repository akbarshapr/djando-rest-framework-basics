from django.urls import path
from . import views
from django import urls


urlpatterns = [
    path('overview/', views.api_overview, name='api_overview'),
    path('product-list/', views.product_list, name='product-list'),
    path('product-create/', views.product_create, name='product-create'),
    path('product-detail/<int:pk>/', views.product_detail, name='product-detail'),
    path('product-update/<int:pk>/', views.product_update, name='product-update'),
    path('product-delete/<int:pk>/', views.product_delete, name='product-delete'),
]
