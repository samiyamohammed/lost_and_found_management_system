# Item Service
**Purpose:** Manages item data.

### Schema:
#### Item
- **Field Name:** `id`
  - **Data Type:** `VARCHAR(255)`
  - **Description:** Unique identifier (UUID)

- **Field Name:** `name`
  - **Data Type:** `VARCHAR(255)`
  - **Description:** Item name

- **Field Name:** `description`
  - **Data Type:** `TEXT`
  - **Description:** Item description

- **Field Name:** `category`
  - **Data Type:** `VARCHAR(255)`
  - **Description:** Item category

- **Field Name:** `status`
  - **Data Type:** `VARCHAR(255)`
  - **Description:** Item status (lost, found)

- **Field Name:** `reported_by`
  - **Data Type:** `VARCHAR(255)`
  - **Description:** Foreign key to User.id

- **Field Name:** `found_by`
  - **Data Type:** `VARCHAR(255)`
  - **Description:** Foreign key to User.id (optional)

- **Field Name:** `created_at`
  - **Data Type:** `DATETIME`
  - **Description:** Timestamp of creation

- **Field Name:** `updated_at`
  - **Data Type:** `DATETIME`
  - **Description:** Timestamp of last update

