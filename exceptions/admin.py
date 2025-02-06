# exceptions/admin.py
from django.contrib import admin
from .models import LogisticsException

admin.site.register(LogisticsException)
