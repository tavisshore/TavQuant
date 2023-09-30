from django.contrib import admin

# Register your models here.
from .models import Stock, Price, Balance, Cash, Income

# ...
admin.site.register(Stock)
admin.site.register(Price)
admin.site.register(Balance)
admin.site.register(Cash)
admin.site.register(Income)