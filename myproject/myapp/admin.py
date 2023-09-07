from django.contrib import admin
from .models import Products,CustomerPreference,Orders

admin.site.register(Products)
admin.site.register(CustomerPreference)
admin.site.register(Orders)

