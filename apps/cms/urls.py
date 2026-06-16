from django.urls import path
from .views import CMSPageView

urlpatterns = [
    path("cms/", CMSPageView.as_view(), name="cms_data"),
]