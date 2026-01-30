from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add_products/', views.add_products, name='add_products'),
    path('cart/',views.cart,name='cart'),
    path('addtocart/<int:pk>/',views.addtocart,name='addtocart'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('update_cart/<int:pk>/<str:op>/',views.update_cart,name='update_cart'),
    path('remove_from_cart/<int:pk>/',views.remove_from_cart,name='remove_from_cart'),
    path('support/',views.support,name='support'),
    path('knowus/',views.knowus,name='knowus'),
]