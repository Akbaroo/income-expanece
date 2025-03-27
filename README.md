# Transaction Management API

- This API allows users to manage their financial transactions. Users can create, retrieve, update, and delete transactions.

## Authentication
All requests require authentication using **Token Authentication**. Include the `Authorization` header with the format:

```http
Authorization: Token <your_token>
```

# Endpoints
## 1️⃣ Get List of Transactions
- **Endpoint**: GET `/api/transactions/`

- **Description**: Retrieves a list of the authenticated user's transactions.

- **Authentication**: Required


### Response Example (`200 OK`):
```json
[
    {
        "id": 1,
        "amount": "500000.00",
        "transaction_type": "income",
        "category": "Salary",
        "date": "2025-03-26T12:34:56Z",
        "description": "March Salary"
    },
    {
        "id": 2,
        "amount": "100000.00",
        "transaction_type": "expense",
        "category": "Food",
        "date": "2025-03-26T15:20:30Z",
        "description": "Lunch purchase"
    }
]
```



## 2️⃣ Create a New Transaction
- **Endpoint**: POST `/api/transactions/`

- **Description**: Creates a new transaction.

- **Authentication**: Required

### Request Example:
```json
{
    "amount": "200000.00",
    "transaction_type": "expense",
    "category": "Transport",
    "description": "Taxi fare"
}
```
### Response Example (`201 Created`):
```json
{
    "id": 3,
    "amount": "200000.00",
    "transaction_type": "expense",
    "category": "Transport",
    "date": "2025-03-26T18:45:10Z",
    "description": "Taxi fare"
}
```

## 3️⃣ Get a Specific Transaction
- **Endpoint**: GET `/api/transactions/{id}/`

- **Description**: Retrieves details of a specific transaction.

- **Authentication**: Required

### Response Example (`200 OK`):
```json
{
    "id": 2,
    "amount": "100000.00",
    "transaction_type": "expense",
    "category": "Food",
    "date": "2025-03-26T15:20:30Z",
    "description": "Lunch purchase"
}
```

## 4️⃣ Update a Transaction
- **Endpoint**: PUT `/api/transactions/{id}/`

- **Description**: Updates an existing transaction.

- **Authentication**: Required

### Request Example:
```json
{
    "amount": "120000.00",
    "transaction_type": "expense",
    "category": "Food",
    "description": "Dinner purchase"
}
```
### Response Example (`200 OK`):
```json
{
    "id": 2,
    "amount": "120000.00",
    "transaction_type": "expense",
    "category": "Food",
    "date": "2025-03-26T15:20:30Z",
    "description": "Dinner purchase"
}
```

## 5️⃣ Delete a Transaction
- **Endpoint**: DELETE `/api/transactions/{id}/`

- **Description**: Deletes a transaction.

- **Authentication**: Required

### Response Example (`204 No Content`):
`No response body.`

### Error Response (`404 Not Found`):
```json
{
    "error": "Transaction not found"
}
```

# Notes
- Transactions are linked to the authenticated user, so users can only manage their own transactions.

- The date field is automatically assigned when creating a transaction.

- Filtering options can be added if needed.



