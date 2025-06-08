from django.urls import path
from .views import PaystackInitializeAPIView, PaystackVerifyAPIView, PaystackWebhookAPIView

urlpatterns = [
    path('payments/', PaystackInitializeAPIView.as_view()), # , name='payments'),
    path('payments/<str:reference>/', PaystackVerifyAPIView.as_view()), # , name='payments'),
    path('payments/webhook/', PaystackWebhookAPIView.as_view())
]