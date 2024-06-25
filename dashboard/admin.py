from django.contrib import admin
from .models import Asset, Order # type: ignore

admin.site.register(Asset)
admin.site.register(Order)
