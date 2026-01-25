from decimal import Decimal
from django.db import models
from project import settings

User = settings.AUTH_USER_MODEL


class PricingSection(models.Model):
    title = models.CharField(max_length=255, default="Unlock Premium Healing", null=True, blank=True)
    subtitle = models.CharField(max_length=255, default="Unlimited healing sessions, anytime", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or "Title"

class PlanItem(models.Model):
    BILLING_CHOICES = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]

    pricing = models.ForeignKey(PricingSection, on_delete=models.CASCADE, related_name="plan_items", null=True, blank=True)
    billing_cycle = models.CharField(max_length=20, choices=BILLING_CHOICES, default="monthly") 
    monthly_price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_percent = models.PositiveIntegerField(default=0, help_text="Only applicable for yearly plans")
    heading = models.CharField(max_length=100, null=True, blank=True, default="Premium Benefits")
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def yearly_price(self):
        if self.billing_cycle == "monthly":
            return self.monthly_price

        yearly_base = self.monthly_price * Decimal(12)
        discount = (yearly_base * self.discount_percent) / Decimal(100)
        final_price = yearly_base - discount
        return final_price.quantize(Decimal('0.01'))

    def __str__(self):
        return f"{self.billing_cycle} plan"

class Features(models.Model):
    planitem = models.ForeignKey(PlanItem, on_delete=models.CASCADE, related_name="features", null=True, blank=True)
    text = models.CharField(max_length=255, null=True, blank=True)
    include = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text or "Features Text"


class Subscription(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("canceled", "Canceled"),
        ("expired", "Expired"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_item = models.ForeignKey(PlanItem, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.plan}"