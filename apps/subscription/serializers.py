from rest_framework import serializers
from .models import PlanItem, Features

# PlanItem Features
class FeaturesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Features
        fields = [
            'order',
            'text', 
            'include',

        ]

# PlanItem
class PlanItemSerializer(serializers.ModelSerializer): 
    features = FeaturesSerializer(many=True, read_only=True)

    class Meta:
        model = PlanItem
        fields = [
            'id', 
            'billing_cycle',
            'price',
            'is_active', 
            'features',

        ]
