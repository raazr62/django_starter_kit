from django.urls import path
from .views import PlanItemView

urlpatterns = [
    path('subscription/packages/', PlanItemView.as_view(), name='plan-item'),
]