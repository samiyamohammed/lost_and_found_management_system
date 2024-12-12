# Notification Management Service

## API Purpose:
Sends notifications to users about updates on items (e.g., when a match is found).

---

## Endpoints:

### 1. Send Notification

**Endpoint:** `POST /notifications/send`

**Description:** Sends a notification to a user (e.g., when their lost item is found).

**Request Body:**
```json
{
  "user_id": "uuid-1234",
  "message": "Your lost wallet has been found!",
  "status": "pending"
}
```

**Response:**

- **Success (201):**
  ```json
  {
    "id": "notification-uuid-7890",
    "user_id": "uuid-1234",
    "message": "Your lost wallet has been found!",
    "status": "pending",
    "created_at": "2024-12-09T01:00:00Z"
  }
  ```

- **Failure (400):**
  ```json
  {
    "error": "Invalid notification data"
  }
  ```

---

### 2. Get Notification History

**Endpoint:** `GET /notifications/{user_id}`

**Description:** Fetch a user's notification history.

**Request Params:** `{user_id}` (path parameter)

**Response:**

- **Success (200):**
  ```json
  [
    {
      "id": "notification-uuid-7890",
      "user_id": "uuid-1234",
      "message": "Your lost wallet has been found!",
      "status": "sent",
      "created_at": "2024-12-09T01:00:00Z"
    }
  ]
  ```

- **Failure (404):**
  ```json
  {
    "error": "User not found or no notifications"
  }
  
