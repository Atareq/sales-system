# Generated by Django 4.2.6 on 2023-11-12 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('receipt', '__first__'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TraderReceiptProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peices', models.IntegerField(default=1, null=True)),
                ('cartons', models.IntegerField(null=True)),
                ('profit_of_piece', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receipt.traderreceipt')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerReceiptProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peices', models.IntegerField(default=1, null=True)),
                ('cartons', models.IntegerField(null=True)),
                ('profit_of_piece', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receipt.customerreceipt')),
            ],
        ),
    ]
