from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'



class InvoiceDetailSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer() 
    invoice = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all())  # Include a link to the related Invoice
    class Meta:
        model = InvoiceDetail
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Check if this is a read operation (e.g., GET request)
        if self.context['request'].method == 'GET':
            # Include InvoiceSerializer data in read operations
            invoice_data = InvoiceSerializer(instance.invoice).data
            data['invoice'] = invoice_data

        return data