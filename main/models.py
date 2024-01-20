from django.db import models
from main.functions import slugify
from django.contrib.auth.models import User
# Create your models here.


class Cars(models.Model):

    car_model = models.CharField(verbose_name='Модель автомобиля', max_length=255, default='Модель №1')
    slug = models.SlugField(verbose_name='URL', unique=True, db_index=True, max_length=255)
    price = models.IntegerField(verbose_name='Стоимость (руб./час)', default=99999)
    description = models.TextField(verbose_name='Сведения', max_length=1000, default='', blank=True)
    photo = models.FileField(verbose_name='Изображение', upload_to='cars/', default='', blank=True)

    def __str__(self):
        return self.car_model

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.car_model)
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Orders(models.Model):

    creation_date = models.DateTimeField(verbose_name='Дата заказа', auto_now_add=True)
    client = models.ForeignKey(User, verbose_name='Клиент', to_field='id', on_delete=models.DO_NOTHING)
    car = models.ForeignKey(Cars, verbose_name='Автомобиль', to_field='id', on_delete=models.DO_NOTHING)
    rent_time = models.IntegerField(verbose_name='Время аренды (в минутах)', default=600)
    total_price = models.IntegerField(verbose_name='Общая сумма', default=-1, editable=False)

    def _calculate_total_price(self):
        MINUTES_IN_HOUR = 60
        return (self.rent_time / MINUTES_IN_HOUR) * self.car.price + \
               (self.rent_time % MINUTES_IN_HOUR) * (self.car.price / MINUTES_IN_HOUR)

    def __str__(self):
        return "Заказ №" + str(self.id)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.total_price = self._calculate_total_price()
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-id']


