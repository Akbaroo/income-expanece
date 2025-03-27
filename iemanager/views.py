from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]  # فقط کاربران لاگین کرده می‌توانند استفاده کنند

    def get(self, request):
        """ دریافت لیست تراکنش‌های کاربر """
        transactions = Transaction.objects.filter(user=request.user)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """ ایجاد یک تراکنش جدید """
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # کاربر را از `request` تنظیم می‌کنیم
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        """ دریافت یک تراکنش خاص که متعلق به کاربر فعلی باشد """
        try:
            return Transaction.objects.get(pk=pk, user=user)
        except Transaction.DoesNotExist:
            return None

    def get(self, request, pk):
        """ دریافت جزئیات یک تراکنش """
        transaction = self.get_object(pk, request.user)
        if transaction is None:
            return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, pk):
        """ بروزرسانی تراکنش """
        transaction = self.get_object(pk, request.user)
        if transaction is None:
            return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """ حذف تراکنش """
        transaction = self.get_object(pk, request.user)
        if transaction is None:
            return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)

        transaction.delete()
        return Response({'message': 'Transaction deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
