# from django.test import TestCase

# Create your tests here.

# payments/tests/test_payments_api.py

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.utils.timezone import now
from unittest.mock import patch, MagicMock
import json
from .models import PaymentTransaction as Transaction

# ---- Initialize Transaction Test ----

# payments/tests/test_payments_api.py (add this class)

from unittest.mock import patch, MagicMock
from django.utils.timezone import now
from rest_framework.test import APITestCase
from rest_framework import status

class VerifyTransactionAPITest(APITestCase):
    def setUp(self):
        # Create a fake transaction in DB
        self.transaction = Transaction.objects.create(
            email='verifytest@example.com',
            amount=5000,
            reference='test_ref_12345',
            status='pending'
        )

    @patch('payments.views.requests.get')
    def test_verify_transaction(self, mock_get):
        # Arrange → set up fake Paystack verify response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": True,
            "message": "Verification successful",
            "data": {
                "reference": self.transaction.reference,
                "amount": 500000,  # Paystack sends amount in kobo
                "status": "success",
                "paid_at": now().isoformat(),
                "other_fields": "..."  # can ignore the rest
            }
        }
        mock_get.return_value = mock_response

        # Act → call the API
        url = f'/api/v1/payments/{self.transaction.reference}/'

        response = self.client.get(url)

        print("Verify transaction response:", response.json())

        # Assert → check clean transformed response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['reference'], self.transaction.reference)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(response.data['amount'], 5000)  # converted from 500000 kobo
        self.assertIsNotNone(response.data['paid_at'])

        # Verify DB updated
        self.transaction.refresh_from_db()
        self.assertEqual(self.transaction.status, 'success')
        self.assertEqual(self.transaction.amount, 5000)

class VerifyTransactionAPITest(APITestCase):
    def setUp(self):
        # Create a fake transaction in DB
        self.transaction = Transaction.objects.create(
            email='verifytest@example.com',
            amount=5000,
            reference='test_ref_12345',
            status='pending'
        )

    @patch('payments.views.requests.get')
    def test_verify_transaction(self, mock_get):
        # Arrange → set up fake Paystack verify response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": True,
            "data": {
                "reference": self.transaction.reference,
                "amount": 500000,  # Paystack sends amount in kobo
                "status": "success",
                "paid_at": now().isoformat()
            }
        }
        mock_get.return_value = mock_response

        # Act → call the API
        url = f'/api/v1/payments/{self.transaction.reference}/'

        response = self.client.get(url)

        print("Verify transaction response:", response.json())

        # Assert → check results
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('reference', response.data)
        self.assertEqual(response.data['reference'], self.transaction.reference)
        self.assertEqual(response.data['status'], 'success')

        # Verify that requests.get was called
        mock_get.assert_called_once()

# ---- Paystack Webhook Test ----

class PaystackWebhookAPITest(APITestCase):
    def setUp(self):
        # Create a transaction that will be updated by the webhook
        self.transaction = Transaction.objects.create(
            email='webhooktest@example.com',
            amount=5000,
            reference='webhook_ref_12345',
            status='pending'
        )

    def test_webhook_charge_success(self):
        url = '/api/v1/payments/webhook/'

        payload = {
            "event": "charge.success",
            "data": {
                "reference": self.transaction.reference,
                "amount": 500000,  # Paystack amount in kobo
                "paid_at": now().isoformat()
            }
        }

        response = self.client.post(
            url,
            data=json.dumps(payload),
            content_type='application/json'
        )

        print("Webhook response:", response.json())

        # Assert → check response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Reload transaction from DB
        self.transaction.refresh_from_db()

        # Assert → transaction status updated
        self.assertEqual(self.transaction.status, 'success')
