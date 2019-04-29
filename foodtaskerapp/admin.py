from django.contrib import admin
from .models import Restaurant, Driver, Customer
# Register your models here.


admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Driver)

