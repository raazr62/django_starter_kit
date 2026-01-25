from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PricingSection
from .serializers import PricingSectionSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status


class PricingListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        pricing_sections = PricingSection.objects.all().prefetch_related('plan_items__features')
        serializer = PricingSectionSerializer(pricing_sections, many=True)

        return Response({
            "status": status.HTTP_200_OK,
            "success": True,
            "message": "Pricing sections retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    