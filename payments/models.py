from django.db import models

from courses.models import Course
from users.models import User
# Create your models here.


class paymentIntent(models.Model):
    payment_intent_id=models.CharField(max_length=225)
    checkout_id=models.CharField(max_length=225)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    course=models.ManyToManyField(Course)
    created=models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    payment_intent=models.ForeignKey(paymentIntent, on_delete=models.CASCADE)
    total_amount=models.DecimalField(max_digits=15, decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)
