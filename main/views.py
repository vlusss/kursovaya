from django.contrib.auth import login as user_login
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.core.checks import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect

from main.forms import UserRegisterForm, UserEditForm, MakeOrderForm
from main.models import Cars, Orders
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def cars(request):
    _cars = Cars.objects.all()
    context = {
        'cars': _cars,
    }
    return render(request, 'main/cars.html', context)


def car_by_id(request, car_id):
    car = get_object_or_404(Cars, pk=car_id)
    form = MakeOrderForm()
    context = {
        'car': car,
        'form': form,
    }
    return render(request, 'main/car.html', context)


def car_by_slug(request, car_slug):
    car = get_object_or_404(Cars, slug=car_slug)
    form = MakeOrderForm()
    context = {
        'car': car,
        'form': form,
    }
    return render(request, 'main/car.html', context)


def about(request):
    return render(request, 'main/about.html')


def order(request):
    if request.POST:
        if request.user:
            _car = request.POST['car']
            _time = int(request.POST['rent_time'])
            client = get_object_or_404(User, pk=request.user.id)
            car = get_object_or_404(Cars, pk=_car)
            order_data = Orders.objects.create(client=client, car=car, rent_time=_time)
            context = {
                'order': order_data
            }
            return render(request, 'main/order.html', context)
        else:
            raise PermissionDenied()
    else:
        raise PermissionDenied()


def profile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)
        if request.method == "POST":
            user_form = UserEditForm(request.POST, instance=user)
            if user_form.is_valid():
                user_form.save()
        else:
            user_form = UserEditForm(instance=user)
        user_orders = Orders.objects.filter(client=user)
        context = {
            'user_orders': user_orders,
            'form': user_form
        }
        return render(request, 'main/profile.html', context)
    else:
        raise PermissionDenied()


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            user_login(request, user)
        return render(request, 'registration/registration.html', {'form': form, 'success_reg': True})
    else:
        form = UserRegisterForm()
    return render(request, 'registration/registration.html', {'form': form})


def login(request):
    form = LoginView()
    return render(request, 'registration/login.html', {'form': form})
