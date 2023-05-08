from django.urls import path
from catalogue import views

urlpatterns = [
    path('product/list/', views.product_list, name='product-list'),
    path('product/detail/<int:pk>', views.product_detail, name='product-detail'),
    path('user/', views.user, name='user')

]
