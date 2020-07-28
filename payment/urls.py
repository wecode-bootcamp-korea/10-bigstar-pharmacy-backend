from django.urls import path

from .views import PaymentView, PaymentTogo, MyPilly

urlpatterns = [
    path('payment',PaymentView.as_view(), name='payment'),
    path('payment/togo', PaymentTogo.as_view(), name='payment_togo'),
    path('mypilly', MyPilly.as_view(), name='mypilly'),
]

