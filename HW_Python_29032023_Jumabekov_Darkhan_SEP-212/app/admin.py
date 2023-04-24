from django.contrib import admin
from .models import Authors, Books, Publishers, Publications, Sales

# Register your models here.

admin.site.register([Authors, Books, Publishers, Publications, Sales])
