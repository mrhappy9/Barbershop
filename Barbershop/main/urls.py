from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us', views.about, name='about'),
    path('pricing', views.pricing, name='pricing'),
    path('order', views.order, name='order'),
    path('login', views.login_page, name='login'),
    path('register', views.register_page, name='register'),
    path('create_book', views.create_book, name='create_book'),
    path('customer_page', views.customer_page, name='customer_page'),
    path('customer_info', views.customer_info, name='customer_info'),
]
