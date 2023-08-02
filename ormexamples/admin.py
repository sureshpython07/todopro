from django.contrib import admin
from ormexamples.models import Customer,Vehicle,Customer_one,Vehicle_many,Worker,Machine

# Register your models here.
admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(Customer_one)
admin.site.register(Vehicle_many)
admin.site.register(Worker)
admin.site.register(Machine)