from rest_framework import serializers
from .models import PricingSection, PlanItem, Features

class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = [
            'id', 
            'text', 
            'include', 
            'order'
        ]

class PlanItemSerializer(serializers.ModelSerializer):
    features = FeaturesSerializer(many=True, read_only=True)
    yearly_price = serializers.SerializerMethodField()

    class Meta:
        model = PlanItem
        fields = [
            'id', 
            'billing_cycle',
            'yearly_price',
            'monthly_price',
            'is_active', 
            'features'
        ]
    
    def get_yearly_price(self, obj):
        return obj.yearly_price

class PricingSectionSerializer(serializers.ModelSerializer):
    plan_items = PlanItemSerializer(many=True, read_only=True)

    class Meta:
        model = PricingSection
        fields = [
            'id', 
            'title', 
            'subtitle', 
            'plan_items'
        ]