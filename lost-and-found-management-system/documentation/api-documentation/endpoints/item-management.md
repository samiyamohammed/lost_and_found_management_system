#Item Management Service
API Purpose:
Manages lost and found items, including reporting, searching, and updating item status.

##Endpoints:

###Report Lost or Found Item

**Endpoint:** POST /items/report
**Description:** Reports a lost or found item.
**Request Body:**
json

{
  "name": "Wallet",
  "description": "Black leather wallet, contains ID and credit cards",
  "category": "Personal Items",
  "status": "lost",
  "reported_by": "uuid-1234"
}
**Response:**

Success (201):
json

{
  "id": "item-uuid-5678",
  "name": "Wallet",
  "status": "lost",
  "reported_by": "uuid-1234",
  "created_at": "2024-12-09T00:00:00Z"
}
Failure (400):
json

{
  "error": "Invalid item data"
}


####Search Items

**Endpoint:** GET /items
**Description:** Allows users to search for lost or found items with filters like category, status, etc.
**Request Params:**
status (optional): Filter by item status (e.g., "lost", "found").
category (optional): Filter by category.
**Response:**
Success (200):
json

[
  {
    "id": "item-uuid-5678",
    "name": "Wallet",
    "description": "Black leather wallet, contains ID and credit cards",
    "status": "lost",
    "reported_by": "uuid-1234",
    "found_by": null,
    "created_at": "2024-12-09T00:00:00Z"
  }
]
Failure (400):
json

{
  "error": "Invalid search parameters"
}


####Update Item Status

**Endpoint:** PUT /items/{item_id}
**Description:** Update the status of a reported item (e.g., from "lost" to "found").
**Request Params:** {item_id} (path parameter)
**Request Body:**
json
{
  "status": "found",
  "found_by": "uuid-5678"
}
**Response:**
Success (200):
json

{
  "id": "item-uuid-5678",
  "name": "Wallet",
  "status": "found",
  "found_by": "uuid-5678",
  "updated_at": "2024-12-09T01:00:00Z"
}
Failure (404):
json

{
  "error": "Item not found"
}
