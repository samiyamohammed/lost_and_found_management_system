#User Management Service
**API Purpose:**
Handles user registration, login, and profile management.

###Endpoints:
####User Registration

**Endpoint:** POST /users/register
**Description:** Registers a new user.
**Request Body:**
json

{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "password": "securepassword"
}
**Response:**
Success (201):
json

{
  "id": "uuid-1234",
  "name": "John Doe",
  "email": "john.doe@example.com",
  "message": "User created successfully"
}
Failure (400):
json

{
  "error": "Email is already in use"
}

####User Login

**Endpoint**: POST /users/login
**Description:** Authenticates a user and returns a JWT token.
**Request Body:**
json

{
  "email": "john.doe@example.com",
  "password": "securepassword"
}
**Response:**
Success (200):
json

{
  "token": "jwt-token-abc123"
}
Failure (401):
json

{
  "error": "Invalid credentials"
}


####Get User Profile

**Endpoint:** GET /users/{user_id}
**Description:** Fetches a user's profile by their unique ID.
**Request Params:** {user_id} (path parameter)
**Response:**
Success (200):
json

{
  "id": "uuid-1234",
  "name": "John Doe",
  "email": "john.doe@example.com",
  "role": "user",
  "created_at": "2024-01-01T00:00:00Z"
}
Failure (404):
json

{
  "error": "User not found"
}
