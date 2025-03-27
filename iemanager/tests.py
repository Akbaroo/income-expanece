from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()




class TransactionTests(APITestCase):
    def setUp(self):
        """Create a test user and get authentication token"""
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.transaction_data = {
            "amount": "50000.00",
            "transaction_type": "expense",
            "category": "Food",
            "description": "Lunch",
        }

    def test_create_transaction(self):
        """Test creating a new transaction"""
        response = self.client.post(
            "/api/transactions/", self.transaction_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["amount"], self.transaction_data["amount"])

    def test_get_transactions(self):
        """Test retrieving transactions list"""
        self.client.post("/api/transactions/", self.transaction_data, format="json")
        response = self.client.get("/api/transactions/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_transaction(self):
        """Test updating a transaction"""
        create_response = self.client.post(
            "/api/transactions/", self.transaction_data, format="json"
        )
        transaction_id = create_response.data["id"]
        update_data = {
            "amount": "60000.00",
            "transaction_type": "expense",
            "category": "Dinner",
            "description": "Updated Dinner",
        }
        response = self.client.put(
            f"/api/transactions/{transaction_id}/", update_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["amount"], update_data["amount"])

    def test_delete_transaction(self):
        """Test deleting a transaction"""
        create_response = self.client.post(
            "/api/transactions/", self.transaction_data, format="json"
        )
        transaction_id = create_response.data["id"]
        response = self.client.delete(f"/api/transactions/{transaction_id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
