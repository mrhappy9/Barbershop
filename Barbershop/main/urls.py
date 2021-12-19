from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us', views.contact, name='contact'),
    path('order', views.order, name='order'),
    path('login', views.login_page, name='login'),
    path('register', views.register_page, name='register'),
    path('create_book', views.create_book, name='create_book'),
    path('customer_page', views.customer_page, name='customer_page'),
    path('customer_info', views.customer_info, name='customer_info'),
    path('barber_book', views.barber_book, name='barber_book'),
]
