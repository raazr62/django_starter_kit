from django.contrib import admin
from .models import SubscriptionPackage, Features
from unfold.admin import ModelAdmin, TabularInline


# Subscription Package Features
class FeaturesInline(TabularInline):
    model = Features
    extra = 0
    ordering_field = "order" # enables drag-and-drop sorting
    hide_ordering_field = False
    fields = ("text", "include", "order")  # keep order included (required)

    class Media:
        js = ("admin/js/feature_order_autofill.js",)

# Subscription Package
@admin.register(SubscriptionPackage)
class SubscriptionPackageAdmin(ModelAdmin):
    list_display = ('billing_cycle', 'price', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'billing_cycle')
    search_fields = ('billing_cycle', 'price')
    inlines = [FeaturesInline]

    fieldsets = (
        (None, {
            'fields': (
                'billing_cycle_type', 
                'billing_cycle', 
                'custom_days', 
                'price', 
                'is_active',
                )
        }),
    )

    class Media:
        js = ("admin/js/planitem_billing_toggle.js",)
