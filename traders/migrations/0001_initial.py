# Generated by Django 4.2.6 on 2023-11-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trader', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=60)),
                ('debut', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
