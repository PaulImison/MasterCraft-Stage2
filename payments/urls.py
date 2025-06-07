from django.urls import path
from .views import PaystackInitializePaymentView, PaystackVerifyPaymentView

urlpatterns = [
    path('payments/', PaystackInitializePaymentView.as_view()), # , name='payments'),
    path('payments/<str:reference>/', PaystackVerifyPaymentView.as_view()), # , name='payments'),
]