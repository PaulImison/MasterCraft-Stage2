from django.db import models

# Create your models here.
class PaymentTransaction(models.Model):
    reference = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.IntegerField(help_text="Amount in kobo")
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.reference} - {self.status}"
    
    # def amount_in_kshs(self):
    #     return self.amount / 100

