from django.db import models
from django.utils import timezone

class Good(models.Model):
    goods_name = models.CharField(max_length=200, verbose_name=u"Название товара")
    goods_description = models.TextField(blank=True, verbose_name=u"Описание")
    goods_number_in_box = models.IntegerField(blank=True, verbose_name=u"Количество в ящике")
    goods_weight = models.IntegerField( blank=True, verbose_name=u"Средний вес")
    goods_kind = models.ForeignKey('goods.Type', verbose_name=u"Тип яйца")
    goods_photo_url = models.CharField(max_length=1000, blank=True, verbose_name=u"Ссылка на фото")
    goods_price = models.FloatField(max_length=10, blank=True, verbose_name=u"Цена (пр: 6,4)")

    def __str__(self):
        return self.goods_name

class Type(models.Model):
    type_name = models.CharField(max_length=1000, verbose_name=u"Тип яйца")

    def __str__(self):
        return self.type_name

class Purchases(models.Model):
    purchases_good = models.ForeignKey('goods.Good', verbose_name=u"Товар")
    purchases_count = models.IntegerField(blank=True, verbose_name=u"Количество товара")
    purchases_summ = models.FloatField(max_length=1000000, blank=True, verbose_name=u"Сумма")
    purchases_date = models.DateTimeField(default=timezone.now, blank=True, verbose_name=u"Дата и время покупки")

    def __str__(self):
        return self.purchases_date

class UsersInSite(models.Model):
    user_name = models.CharField(max_length=200, blank=True, verbose_name=u"Пользователь")
    user_password = models.CharField(max_length=128, blank=True, verbose_name=u"Пароль")
    user_fio = models.CharField(max_length=200, blank=True, verbose_name=u"ФИО")
    user_phone = models.CharField(max_length=15, blank=True, verbose_name=u"Телефон")
    user_purchase = models.ForeignKey('goods.Purchases', blank=True, verbose_name=u"Покупка")

    def __str__(self):
        return self.user_name

class Contacts(models.Model):
    phone1 = models.IntegerField(verbose_name=u"Телефон")
    phone2 = models.IntegerField(blank=True, verbose_name=u"Телефон2 не обязательный")
    phone3 = models.IntegerField(blank=True, verbose_name=u"Телефон3 не обязательный")
    phone4 = models.IntegerField(blank=True, verbose_name=u"Телефон4 не обязательный")
    phone5 = models.IntegerField(blank=True, verbose_name=u"Телефон5 не обязательный")
    address = models.CharField(max_length=300, blank=True, verbose_name=u"Адрес")
    address2 = models.CharField(max_length=300, blank=True, verbose_name=u"Адрес2")
    email = models.CharField(max_length=50, blank=True, verbose_name=u"Эл. почта")

    def __str__(self):
        return self.phone1
