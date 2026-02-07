from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SubscriptionPackage
from .serializers import SubscriptionPackageSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

# Subscription Package List
class SubscriptionPackageView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try: 
            subscription_packages = SubscriptionPackage.objects.filter(is_active=True).prefetch_related('features')
            serializer = SubscriptionPackageSerializer(subscription_packages, many=True)

            return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Active subscription packages retrieved successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "success": False,
                "message": f"An error occurred: {str(e)}",
                "data": None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

