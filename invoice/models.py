from django.db import models

# Create your models here.


class Invoice(models.Model):
    customer_name= models.CharField(max_length=100, null= True, blank= True)
    date= models.DateField()

    def __str__(self) -> str:
        return self.customer_name

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_details')
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)