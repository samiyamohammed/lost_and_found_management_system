
# Notification Service
**Purpose:** Manages notifications.

### Schema:
#### Notification
- **Field Name:** `id`
  - **Data Type:** `VARCHAR(255)`
  - **Description:** Unique identifier (UUID)

- **Field Name:** `user_id`
  - **Data Type:** `VARCHAR(255)`
  - **Description:** Foreign key to User.id

- **Field Name:** `message`
  - **Data Type:** `TEXT`
  - **Description:** Notification message

- **Field Name:** `status`
  - **Data Type:** `VARCHAR(255)`
  - **Description:** Notification status (pending, sent, delivered)

- **Field Name:** `created_at`
  - **Data Type:** `DATETIME`
  - **Description:** Timestamp of creation
