# payments/urls.py
from django.urls import path
from .views import stk_push_success

urlpatterns = [
    path('stk-push/', stk_push_success, name='stk_push'),  # URL to handle the STK Push
]
