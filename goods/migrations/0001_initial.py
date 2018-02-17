# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-02 18:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=200)),
                ('goods_description', models.TextField()),
                ('goods_number_in_box', models.IntegerField(max_length=1000)),
                ('goods_weight', models.IntegerField(max_length=1000)),
                ('goods_kind', models.CharField(max_length=50)),
                ('goods_photo_url', models.CharField(max_length=1000)),
                ('goods_price', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchases_count', models.IntegerField(max_length=1000000)),
                ('purchases_summ', models.FloatField(max_length=1000000)),
                ('purchases_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('purchases_good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Good')),
            ],
        ),
        migrations.CreateModel(
            name='UsersInSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_password', models.CharField(max_length=128)),
                ('user_fio', models.CharField(max_length=200)),
                ('user_phone', models.CharField(max_length=15)),
                ('user_purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Purchases')),
            ],
        ),
    ]