from django.contrib import admin
import nested_admin
from .models import PricingSection, PlanItem, Features


# Features PlanItem inline
class FeaturesInline(nested_admin.NestedTabularInline):
    model = Features
    extra = 1

# PlanItem PricingSection inline
class PlanItemInline(nested_admin.NestedTabularInline):
    model = PlanItem
    extra = 1
    inlines = [FeaturesInline]

# PlanItem (Top-level admin)
@admin.register(PlanItem)
class PlanItemAdmin(nested_admin.NestedModelAdmin):
    list_display = (
        'id',
        'billing_cycle',
        'yearly_price',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = ('billing_cycle', 'is_active')
    search_fields = ('id',)
    inlines = [FeaturesInline]

# PricingSection (Root admin)
@admin.register(PricingSection)
class PricingSectionAdmin(nested_admin.NestedModelAdmin):
    list_display = (
        'id',
        'title',
        'subtitle',
        'created_at',
        'updated_at',
    )
    search_fields = ('title', 'subtitle')
    ordering = ('created_at',)
    inlines = [PlanItemInline]
