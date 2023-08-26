from django.urls import path
from django.views.decorators.cache import cache_page

from app_csv.views import StonesView

urlpatterns = [
    path('app', cache_page(60)(StonesView.as_view()))
]