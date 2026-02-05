from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PlanItem
from .serializers import PlanItemSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

# PlanItem List
class PlanItemView(APIView):
    permission_classes = []

    def get(self, request):
        try: 
            plan_items = PlanItem.objects.filter(is_active=True).prefetch_related('features')
            serializer = PlanItemSerializer(plan_items, many=True)

            return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Active plans retrieved successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "success": False,
                "message": f"An error occurred: {str(e)}",
                "data": None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)