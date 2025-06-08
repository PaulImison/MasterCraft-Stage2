from django.contrib import admin

# Register your models here.
from .models import PaymentTransaction

@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ('name', 'reference', 'email', 'amount', 'status', 'created_at')
    # readonly_fields = ("amount_display",)
    search_fields = ('name', 'reference', 'email', 'status')
    
    # def amount_display(self, obj):
    #     return f"{obj.amount/ 100} Kshs"
    
    # amount_display.short_description = "Actual Amount (Kshs)"