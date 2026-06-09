from django.urls import path
from . import views

urlpatterns = [
   
    path('test-chat/', views.chatbot, name='test_chat'),
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    
    path('checkout/', views.checkout, name='checkout'),
path('order-success/', views.order_success, name='order_success'),

path(
    'increase/<int:cart_id>/',
    views.increase_quantity,
    name='increase_quantity'
),

path(
    'decrease/<int:cart_id>/',
    views.decrease_quantity,
    name='decrease_quantity'
),
path(
    'my-orders/',
    views.my_orders,
    name='my_orders'
),
path(
    'review/<int:product_id>/',
    views.add_review,
    name='add_review'
),

path(
    'chatbot/',
    views.chatbot,
    name='chatbot'
),
]

