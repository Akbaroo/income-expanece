from django.urls import path

from .views import TransactionListCreateAPIView, TransactionDetailAPIView


app_name = 'iemanager'

urlpatterns = [
    path('transactions/', TransactionListCreateAPIView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionDetailAPIView.as_view(), name='transaction-detail'),
]