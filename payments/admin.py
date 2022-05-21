from django.contrib import admin
from .models import Payment,paymentIntent
# Register your models here.


admin.site.register(paymentIntent)
admin.site.register(Payment)