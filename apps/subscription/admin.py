from django.contrib import admin
from .models import PlanItem, Features
from unfold.admin import ModelAdmin, TabularInline


# PlanItem Features
class FeaturesInline(TabularInline):
    model = Features
    extra = 1

    class Media:
        js = ("admin/js/feature_order_autofill.js",)

# PlanItem
@admin.register(PlanItem)
class PlanItemAdmin(ModelAdmin):
    list_display = ('billing_cycle', 'price', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'billing_cycle')
    search_fields = ('billing_cycle', 'price')
    inlines = [FeaturesInline]
