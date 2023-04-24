from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название магазина")
    address = models.CharField(max_length=90, verbose_name="Адрес магазина")
    email = models.EmailField(verbose_name="Эл.почта", null=True)
    created_date = models.DateField(auto_now=True, verbose_name="Дата основания")

    def __str__(self):
        return f"{self.name}, {self.address}"

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.CharField(max_length=200, verbose_name="Описание")
    manufacturer = models.CharField(max_length=100, verbose_name="Производитель")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name="Магазин")

    def __str__(self):
        return f"{self.name}, {self.description}, {self.manufacturer}, {self.price}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']