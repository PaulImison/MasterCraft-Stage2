from django.db import models

# Create your models here.
class PaymentTransaction(models.Model):
    reference = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Amount in kobo")
    status = models.CharField(max_length=20, choices=[
        ("pending", "pending"), 
        ("success", "success"), 
        ("failed", "failed")
        ], default="pending")
    paid_at = models.DateTimeField(null=True, blank=True)    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reference} - {self.status}"
    
    # def amount_in_kshs(self):
    #     return self.amount / 100

