# Generated by Django 3.0.7 on 2020-11-20 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
        migrations.AlterModelTable(
            name='productoption',
            table='product_options',
        ),
        migrations.AlterModelTable(
            name='tag',
            table='tags',
        ),
    ]
