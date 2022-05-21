from django.urls import path

from payments.views import PaymnetHandler,Webhook


urlpatterns = [
        path('webhook/', Webhook.as_view()),
        path("",PaymnetHandler.as_view())
]
