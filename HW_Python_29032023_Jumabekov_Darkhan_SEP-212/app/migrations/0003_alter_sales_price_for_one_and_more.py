# Generated by Django 4.1.4 on 2023-04-01 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_books_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='price_for_one',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Цена одной книги'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='total_price_for_all',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Общая стоимость проданных книг'),
        ),
    ]
