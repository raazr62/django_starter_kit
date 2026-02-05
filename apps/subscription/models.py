from django.db import models
from project import settings

User = settings.AUTH_USER_MODEL

# Subscription Plan Item
class PlanItem(models.Model):
    BILLING_CHOICES = [
        ('7_days', '7 Days'),
        ('14_days', '14 Days'),
        ('30_days', '30 Days'),
    ]

    billing_cycle = models.CharField(max_length=20, choices=BILLING_CHOICES, default="7_days") 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.billing_cycle} plan"

# Features associated with PlanItem
class Features(models.Model):
    plan_item = models.ForeignKey(PlanItem, on_delete=models.CASCADE, related_name="features", null=True, blank=True)
    text = models.CharField(max_length=255, null=True, blank=True)
    include = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text or "Features Text"


# class Subscription(models.Model):
#     STATUS_CHOICES = (
#         ("active", "Active"),
#         ("canceled", "Canceled"),
#         ("expired", "Expired"),
#     )

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     plan_item = models.ForeignKey(PlanItem, on_delete=models.SET_NULL, null=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES)
#     start_date = models.DateTimeField(auto_now_add=True)
#     end_date = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.user} - {self.plan_item}"