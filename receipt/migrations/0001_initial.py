# Generated by Django 4.2.6 on 2023-11-12 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('traders', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TraderReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kinds_number', models.IntegerField(default=0, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('piad', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('rest_of_money', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('trader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='traders.trader')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kinds_number', models.IntegerField(default=0, null=True)),
                ('profit', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('piad', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('rest_of_money', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
