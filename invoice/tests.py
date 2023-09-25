


from django.test import TestCase
from rest_framework.test import APIClient
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_invoice_with_details(self):
        data = {
            "date": "2023-09-24",
            "customer_name": "Test Customer",
            "invoice_details": [
                {
                    "description": "Item 1",
                    "quantity": 2,
                    "unit_price": "10.00",
                    "price": "20.00"
                }

            ]
        }
        response = self.client.post('/invoices/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(InvoiceDetail.objects.count(), 2)

    # Add more test cases for other endpoints and scenarios
