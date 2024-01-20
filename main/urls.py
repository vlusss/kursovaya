from main import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='main'),
    path('cars', views.cars, name='cars'),
    path('cars/<int:car_id>', views.car_by_id, name='car_by_id'),
    path('cars/<slug:car_slug>', views.car_by_slug, name='car_by_slug'),
    path('about', views.about, name='about'),
    path('profile', views.profile, name='profile'),
    path('order', views.order, name='order'),
    path('registration', views.registration, name='registration'),
    path('', include('django.contrib.auth.urls')),
]
