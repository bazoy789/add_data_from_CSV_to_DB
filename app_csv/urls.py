from django.urls import path

from app_csv.views import StonesView

urlpatterns = [
    path('app', StonesView.as_view())
]