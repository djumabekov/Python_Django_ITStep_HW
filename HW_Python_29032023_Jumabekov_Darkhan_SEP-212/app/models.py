from datetime import date

from django.db import models

# Create your models here.

class Authors(models.Model):
    FIO = models.CharField(max_length=100, verbose_name="ФИО")
    birth_date = models.DateField(default=date.today, verbose_name="Дата рождения")

    def __str__(self):
        return f"{self.FIO}, {self.birth_date}"

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['FIO']


class Books(models.Model):
    name = models.CharField(max_length=60, verbose_name="Название книги")
    genre = models.CharField(max_length=60, verbose_name="Жанр")
    write_date = models.DateField(default=date.today, verbose_name="Год написания")
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return f"{self.name}, {self.genre}, {self.write_date}, {self.author}"

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['name']

class Publishers(models.Model):
    name = models.CharField(max_length=60, verbose_name="Название издательства")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'
        ordering = ['name']


class Publications(models.Model):
    count = models.IntegerField(default=1, verbose_name="Тираж")
    date = models.DateField(default=date.today, verbose_name="Дата")
    publisher = models.ForeignKey(Publishers, on_delete=models.CASCADE, verbose_name="Издательство")
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name="Книга")

    def __str__(self):
        return f"{self.book}, {self.publisher}, {self.date}, {self.count}"

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['date']


class Sales(models.Model):
    price_for_one = models.DecimalField(default=0, max_digits=6, decimal_places=2, verbose_name="Цена одной книги")
    total_price_for_all = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name="Общая стоимость проданных книг")
    count = models.IntegerField(default=0, verbose_name="Количество проданных книг")
    date = models.DateField(default=date.today, verbose_name="Дата")
    publications = models.ForeignKey(Publications, on_delete=models.CASCADE, verbose_name="Публикации")

    def __str__(self):
        return f"{self.publications}, {self.date}, {self.count}, {self.price_for_one}, {self.total_price_for_all}"

    class Meta:
        verbose_name = 'Годовая продажа'
        verbose_name_plural = 'Годовые продажи'
        ordering = ['date']