from django.urls import path
from .views import SubscriptionPackageView

urlpatterns = [
    path('subscription/packages/', SubscriptionPackageView.as_view(), name='subscription-package'),
]