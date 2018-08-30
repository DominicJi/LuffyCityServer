# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-17 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('api', '0004_coupon_couponrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.SmallIntegerField(choices=[(0, '微信'), (1, '支付宝'), (2, '优惠码'), (3, '贝里')])),
                ('payment_number', models.CharField(blank=True, max_length=128, null=True, verbose_name='支付第3方订单号')),
                ('order_number', models.CharField(max_length=128, unique=True, verbose_name='订单号')),
                ('actual_amount', models.FloatField(verbose_name='实付金额')),
                ('status', models.SmallIntegerField(choices=[(0, '交易成功'), (1, '待支付'), (2, '退费申请中'), (3, '已退费'), (4, '主动取消'), (5, '超时取消')], verbose_name='状态')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='订单生成时间')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='付款时间')),
                ('cancel_time', models.DateTimeField(blank=True, null=True, verbose_name='订单取消时间')),
            ],
            options={
                'verbose_name_plural': '37. 订单表',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('original_price', models.FloatField(verbose_name='课程原价')),
                ('price', models.FloatField(verbose_name='折后价格')),
                ('content', models.CharField(blank=True, max_length=255, null=True)),
                ('valid_period_display', models.CharField(max_length=32, verbose_name='有效期显示')),
                ('valid_period', models.PositiveIntegerField(verbose_name='有效期(days)')),
                ('memo', models.CharField(blank=True, max_length=255, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Order')),
            ],
            options={
                'verbose_name_plural': '38. 订单详细',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='bely',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
        migrations.AlterUniqueTogether(
            name='orderdetail',
            unique_together=set([('order', 'content_type', 'object_id')]),
        ),
    ]
