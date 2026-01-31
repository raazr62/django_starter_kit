from django.urls import path
from .views import PricingListView

urlpatterns = [
    path('subscription/packages/', PricingListView.as_view(), name='pricing-list'),
]