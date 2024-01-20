from django.contrib import admin
from main.models import Cars, Orders

# Register your models here.


class AdminCars(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("car_model",)}


class AdminOrders(admin.ModelAdmin):
    readonly_fields = ('total_price', )


admin.site.register(Orders, AdminOrders)
admin.site.register(Cars, AdminCars)
