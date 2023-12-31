# Generated by Django 4.2.6 on 2023-11-12 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=40)),
                ('national_id', models.CharField(max_length=14)),
                ('phone_num', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=80)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtract', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
