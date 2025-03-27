from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),  # درآمد
        ('expense', 'Expense')  # هزینه
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)  
    date = models.DateTimeField(auto_now_add=True)  
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.transaction_type} - {self.amount}"