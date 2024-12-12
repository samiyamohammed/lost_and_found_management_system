markdown

Copy
# User Management Service Specifications

## Objective
To handle user registration, login, and profile management.

## Endpoints

### User Registration
- **Endpoint:** `POST /users/register`
- **Description:** Registers a new user.
- **Request Body:**
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "password": "securepassword"
  }
Response:
Success (201):
json

Copy
{
  "id": "uuid-1234",
  "name": "John Doe",
  "email": "john.doe@example.com",
  "message": "User created successfully"
}
Failure (400):
json

Copy
{
  "error": "Email is already in use"
}
User Login
Endpoint: POST /users/login
Description: Authenticates a user and returns a JWT token.
Request Body:
json

Copy
{
  "email": "john.doe@example.com",
  "password": "securepassword"
}
Response:
Success (200):
json

Copy
{
  "token": "jwt-token-abc123"
}
Failure (401):
json

Copy
{
  "error": "Invalid credentials"
}
Get User Profile
Endpoint: GET /users/{user_id}
Description: Fetches a user's profile by their unique ID.
Request Params: {user_id} (path parameter)
Response:
Success (200):
json

Copy
{
  "id": "uuid-1234",
  "name": "John Doe",
  "email": "john.doe@example.com",
  "role": "user",
  "created_at": "2024-01-01T00:00:00Z"
}
Failure (404):
json

Copy
{
  "error": "User not found"
}
Data Formats
All requests and responses will use JSON format.

Error Handling
Errors will be communicated with appropriate HTTP status codes and descriptive messages.
