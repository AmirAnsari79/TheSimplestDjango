from django.urls import path
from catalogue import views
urlpatterns=[
    path('product/list/',views.product_list,name='product-list'),
    path('user/',views.user,name='user')

]