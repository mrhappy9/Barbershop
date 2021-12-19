from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.exceptions import *
from .models import *
from .forms import CreateUserForm, BarbershopOrders, TimeForm, CustomerInformation
from django.contrib.auth.models import (Group, User)
from django.contrib import messages


def home(request):
    context = {}
    barbershops_orders = Order.objects.all()
    barber_names = Order.objects.all().values_list('barber', flat=True).distinct()
    context['times'] = Order.TIME
    context['haircuts'] = Order.HAIRCUTS
    context['orders'] = barbershops_orders
    context['BarberNames'] = barber_names
    context['user'] = request.user

    return render(request, 'main/home.html', context)


def create_book(request):
    form = BarbershopOrders()
    if request.method == 'POST':
        barber = request.POST.get('barber')
        day = request.POST.get('time')
        haircut = request.POST.get('haircuts')
        calendar = request.POST.get('calendar')
        if is_any_value_blank(barber, day, haircut, calendar) is False:
            form = BarbershopOrders(request.POST)
            if form.is_valid():
                form.save()
                order = Order.objects.last()
                order.customer = Customers.objects.get(user=request.user.id)
                order.role = Roles.objects.get(name=barber)
                order.save()

                return redirect('home')

    context = {'form': form, 'user': request.user}
    return render(request, 'main/book_form.html', context)


def customer_info(request):
    context = {}
    form = CustomerInformation()
    if request.method == 'POST':
        customer = Customers.objects.get(user=request.user.id)
        customer.name = request.POST.get('name')
        customer.surname = request.POST.get('surname')
        customer.info = request.POST.get('info')
        customer.save()
        return redirect('customer_page')

    context['form'] = form
    context['user'] = request.user
    return render(request, 'main/customer_info.html', context)


def about(request):
    # return HttpResponse("<h4>About</h4>")
    return render(request, 'main/about.html')


def customer_page(request):
    context = {}
    customers = Customers.objects.all().filter(user=request.user.id)
    context['customers'] = customers
    context['user'] = request.user
    return render(request, 'main/customer.html', context)


def order(request):
    context = {}
    barbershops_orders = []
    barbershops = Order.objects.all()
    for orders in barbershops:
        if orders.customer is not None and orders.customer.user == request.user:
            barbershops_orders.append(orders)
    context['orders'] = barbershops_orders
    context['user'] = request.user

    return render(request, 'main/order.html', context)


def barber_book(request):
    context = {}
    barber_booked = []
    barber_booked_customer = []
    orders = Order.objects.all()
    for book in orders:
        if book.role is not None and book.role.user == request.user:
            barber_booked.append([book, book.customer.name])
            barber_booked_customer.append(book.customer.name)

    context['orders'] = barber_booked
    context['user'] = request.user
    context['orders_customers'] = barber_booked
    print(barber_booked_customer)

    return render(request, 'main/barber_booked.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('home')
    context = {}
    return render(request, 'main/login.html', context)


def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customers.objects.create(
                user=user,
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'main/register.html', context)


def is_any_value_blank(*values):
    return False in [value != '' for value in list(values)]