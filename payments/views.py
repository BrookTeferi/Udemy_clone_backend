from decimal import Decimal
from django.shortcuts import render
import os
import json
from rest_framework.views import APIView
from courses.models import Course
from rest_framework.response import Response
from  rest_framework import status
from rest_framework.permissions import IsAuthenticated
import stripe
from payments.models import Payment, paymentIntent
# Create your views here.
from .models import paymentIntent
from decimal import Decimal
from users.models import User
from django.core.exceptions import ValidationError

STRIPE_APIKEY='sk_test_51KxS3SLd7S41zXwyPQhEuD97sP8uI5tBqkEkvUpNVaYEplAeYJJkpyphRkWZHPW6bZseO4jvxDvK4PvzcGR5RkJ900OS8f5aBH'


stripe_api_key=STRIPE_APIKEY
# stripe_api_key=os.environ.get("STRIPE_APIKEY")
endpoint_secret=''

stripe.api_key=stripe_api_key
class PaymnetHandler(APIView):

    permission_classes=[IsAuthenticated]
    
    def post(self,request):

        if request.body:
            body=json.loads(request.body)
            if body and len(body):
                # fetch course detail as line_items
                courses_line_items=[]
                cart_course=[]
                for item in body:
                    try:
                        course=Course.objects.get(course_uuid=item)

                        line_item={
                            'price_data': {
                            'currency': 'usd',
                            'unit_amount': int(course.price*100),
                            'product_data': {
                                'name': course.title,
                             
                            },
                        },
                            'quantity': 1,
                        }

                        courses_line_items.append(line_item)
                        cart_course.append(course)

                    except Course.DoesNotExist:
                        pass
                    except ValidationError:
                        pass

            else:
                return Response(status=400)
        else:
                return Response(status=400)



        checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=courses_line_items,
                mode='payment',
                success_url='http://localhost:3000/',
                cancel_url="http://localhost:3000/",
                
            )



        intent=paymentIntent.objects.create(
                payment_intent_id=checkout_session.payment_intent,
                checkout_id=checkout_session.id,
                # user=request.user.objects.get(id=1)
                user=User.objects.get(id=1)
                )


        intent.course.add(*cart_course)

        return Response({ "url" : checkout_session.url })

class Webhook(APIView):
    def post(self,request):
        payload=request.body
        sig_header=request.META["HTTP_STRIPE_SIGNITURE"]

        event=None
        try:
            event=stripe.Webhook.construct_event(
                payload=payload,sig_header=sig_header,endpoint_secret=endpoint_secret)
            
        except :
            return Response(status=status.HTTP_401_UNAUTHORIZED)



        if event["type"]=="checkout.session.complete":
            session=event["data"]["object"]

            try:
                intent=paymentIntent.objects.get(checkout_id=session.id, payment_intent_id=session.payment_intent)
            except paymentIntent.DoesNotExist:
                return Response(staus=status.HTTP_400_BAD_REQUEST)

            Payment.objects.create(
                payment_intent=intent,
                total_amount =Decimal(session.amount_total/100)
            )

            intent.user.paid_courses.add(*intent.couse.all())
            return Response (status=200)


        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)