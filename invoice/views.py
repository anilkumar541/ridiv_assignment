from django.shortcuts import render

# Create your views here.


from rest_framework import generics
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def perform_update(self, serializer):
        invoice = self.get_object()

        invoice_details_data = self.request.data.get('invoice_details')
        if invoice_details_data:
            for detail_data in invoice_details_data:
                detail_id = detail_data.get('id', None)
                if detail_id:
                    detail = InvoiceDetail.objects.get(pk=detail_id)
                    detail.description = detail_data.get('description', detail.description)
                    detail.quantity = detail_data.get('quantity', detail.quantity)
                    detail.unit_price = detail_data.get('unit_price', detail.unit_price)
                    detail.price = detail_data.get('price', detail.price)
                    detail.save()
                else:
                    InvoiceDetail.objects.create(invoice=invoice, **detail_data)

class InvoiceDetailListCreateView(generics.ListCreateAPIView):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer

class InvoiceDetailDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer
