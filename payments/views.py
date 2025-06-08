import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils.timezone import now
from .models import PaymentTransaction as Transaction

# DRF view to initialize transaction
class PaystackInitializeAPIView(APIView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        amount = request.data.get('amount')
        
        if not email or not amount:
            return Response({"error": "Email and amount are required."}, status=status.HTTP_400_BAD_REQUEST)

        url = "https://api.paystack.co/transaction/initialize"
        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "email": email,
            "amount": int(amount) * 100,  # amount in kobo
            # "callback_url": "https://mastercraft-stage2.onrender.com/api/v1/payments/callback/"
        }

        response = requests.post(url, json=data, headers=headers)
        res_data = response.json()

        if res_data.get("status"):
            # Save data in DB
            Transaction.objects.create(
                reference=res_data["data"]["reference"],
                name=name,
                email=email,
                amount=amount,
                status='pending'
            )
            
            return Response({
                "authorization_url": res_data["data"]["authorization_url"],
                "access_code": res_data["data"]["access_code"],
                "reference": res_data["data"]["reference"]
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to initialize transaction."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# DRF view to verify transaction (optional if using webhook)
class PaystackVerifyAPIView(APIView):
    def get(self, request, reference):
        # reference = request.query_params.get('reference')
        # reference = reference

        if not reference:
            return Response({"error": "No transaction reference provided."}, status=status.HTTP_400_BAD_REQUEST)

        url = f"https://api.paystack.co/transaction/verify/{reference}"
        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
        }
        response = requests.get(url, headers=headers)
        result = response.json()
        print(result)

        if result.get("status") and result["data"]["status"] == "success":
            # Here you would normally mark order/transaction as paid in your DB
            return Response({
                "status": "success",
                "reference": result["data"]["reference"],
                "amount": result["data"]["amount"] / 100,  # convert back to NGN
                "email": result["data"]["customer"]["email"]
            }, status=status.HTTP_200_OK)
        elif result.get("status") and result["data"]["status"] == "abandoned":
            # Here you would normally mark order/transaction as paid in your DB
            return Response({
                "status": "abandoned",
                "reference": result["data"]["reference"],
                "amount": result["data"]["amount"] / 100,  # convert back to NGN
                "email": result["data"]["customer"]["email"]
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "failed",
                "reference": result.get("data", {}).get("reference"),
                "error": result.get("message")
            }, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class PaystackWebhookAPIView(APIView):
    def post(self, request):
        # Verify Paystack sent this
        paystack_signature = request.headers.get('X-Paystack-Signature')
        # Optionally implement signature verification for security (not shown here)

        payload = request.body
        event = json.loads(payload)

        if event['event'] == 'charge.success':
            reference = event['data']['reference']
            amount_paid = event['data']['amount'] / 100
            paid_at_time = event['data']['paid_at']

            try:
                transaction = Transaction.objects.get(reference=reference)
                transaction.status = 'success'
                transaction.paid_at = now()  # Optional: parse paid_at_time if you want exact timestamp
                transaction.save()

                print(f"Payment successful for {reference}")

            except Transaction.DoesNotExist:
                print(f"Transaction with reference {reference} not found.")

        return Response({"status": "ok"}, status=status.HTTP_200_OK)
