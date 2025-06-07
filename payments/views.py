from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import os
from .models import PaymentTransaction
from dotenv import load_dotenv

load_dotenv()



class PaystackInitializePaymentView(APIView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        amount = request.data.get('amount')
        payStackKey = os.getenv('PAYSTACK_SECRET_KEY', 'PAYSTACK_SECRET_KEY')
        
        headers = {
            "Authorization": f"Bearer {os.getenv('PAYSTACK_SECRET_KEY', 'PAYSTACK_SECRET_KEY')}",
            "Content-Type": "application/json",
        }

        data = {
            "email": email,
            "amount": int(amount) * 100
        }

        response = requests.post("https://api.paystack.co/transaction/initialize", headers=headers, json=data)
        res_data = response.json()

        if response.status_code == 200:
            PaymentTransaction.objects.create(
                reference = res_data["data"]["reference"],
                name=name,
                email=email,
                amount=int(amount) * 100,
                status="pending"
            )
            return Response(res_data, status=status.HTTP_200_OK)
        else:
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
        # return Response(headers, status=status.HTTP_200_OK)

class PaystackVerifyPaymentView(APIView):
    def get(self, request, reference):
        headers = {
            "Authorization": f"Bearer {os.getenv('PAYSTACK_SECRET_KEY', 'PAYSTACK_SECRET_KEY')}",
            "Content-Type": "application/json",
        }

        url = f"https://api.paystack.co/transaction/verify/{reference}"
        response = requests.get(url, headers=headers)
        res_data = response.json()

        try:
            transaction = PaymentTransaction.objects.get(reference=reference)
            customer_name = transaction.name
            tData = {
                "payment": {
                    "id": res_data["data"]["reference"],
                    "customer_name": customer_name,
                    "customer_email": res_data["data"]["customer"]["email"],
                    "amount": res_data["data"]["amount"],
                    "status": res_data["data"]["status"],
                    },
                "message":res_data["data"]["gateway_response"],
                }
            print(tData)
            if response.status_code == 200 and res_data["data"]["status"] == "success":
                transaction.status = "success"
                transaction.save()
            elif response.status_code == 200:
                transaction.status = res_data["data"]["status"]
                transaction.save()
        except PaymentTransaction.DoesNotExist:
            return Response({"error": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)

        return Response(tData, status=response.status_code)
        # return Response(res_data, status=response.status_code)