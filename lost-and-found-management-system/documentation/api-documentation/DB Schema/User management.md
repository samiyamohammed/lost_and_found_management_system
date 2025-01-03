# User Service
**Purpose:** Manages user data.

### Schema:
#### User
- **Field Name:** `id`
  - **Data Type:** `VARCHAR(255)`
  - **Description:** Unique identifier (UUID)

- **Field Name:** `name`
  - **Data Type:** `VARCHAR(255)`
  - **Description:** User's name

- **Field Name:** `email`
  - **Data Type:** `VARCHAR(255)`
  - **Description:** User's email address (unique)

- **Field Name:** `password`
  - **Data Type:** `CHAR(128)`
  - **Description:** Hashed password

- **Field Name:** `role`
  - **Data Type:** `VARCHAR(255)`
  - **Description:** User's role (e.g., user, admin)

- **Field Name:** `created_at`
  - **Data Type:** `DATETIME`
  - **Description:** Timestamp of creation

