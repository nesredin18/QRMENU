# QR Menu SAAS

## Tech Stack: Django

This SAAS application is designed for managing QR menus with user authentication functionalities using Django.

## Table of Contents

# API Reference

## Superuser API
### Register Super User API

- **Description:** Register a superuser with the provided data.

  - **Request Body:**
    ```json
    {
      "email": "superuser@example.com",
      "password": "superuser_password",
      "is_staff": true,
      "is_superuser": true
    }
    ```

  - **Response:**
    - **Success (201 Created):** Superuser registration successful. Returns the newly created superuser details.
      ```json
      {
        "id": 1,
        "username": "superuser@example.com",
        "email": "superuser@example.com"
        // ... other user fields
      }
      ```
    - **Error (4xx):** If registration fails due to validation errors or duplicate entries, an appropriate error response is returned.
      ```json
      {
        "message": "Validation error message"
      }
      ```

## User API

### Register User API

- **Description:** Register a regular user with the provided data.

  - **Request Body:**
    ```json
    {
      "email": "user@example.com",
      "password": "user_password"
    }
    ```

  - **Response:**
    - **Success (201 Created):** User registration successful. Returns the newly created user details.
      ```json
      {
        "id": 2,
        "username": "user@example.com",
        "email": "user@example.com"
        // ... other user fields
      }
      ```
    - **Error (4xx):** If registration fails due to validation errors or duplicate entries, an appropriate error response is returned.
      ```json
      {
        "message": "Validation error message"
      }
      ```

### Login User API

- **Description:** Authenticate a user based on the provided email and password.

  - **Request Body:**
    ```json
    {
      "email": "user@example.com",
      "password": "user_password"
    }
    ```

  - **Response:**
    - **Success (200 OK):** User authentication successful. Returns the user details along with an authentication token.
      ```json
      {
        "id": 2,
        "username": "user@example.com",
        "email": "user@example.com",
        // ... other user fields
        "token": "jwt_token_here"
      }
      ```
    - **Error (4xx):** If login fails due to incorrect credentials or other issues, an appropriate error response is returned.
      ```json
      {
        "message": "Invalid password"
      }
      ```

### User Profile API

- **Description:** Retrieve the profile information of the authenticated user.

  - **Methods:**
    - GET: Retrieve the profile of the authenticated user.

  - **Response:**
    - **Success (200 OK):** Returns the user details.
      ```json
      {
        "id": 2,
        "username": "user@example.com",
        "email": "user@example.com"
        // ... other user fields
      }
      ```

### List Non-Superusers API

- **Description:** Retrieve a list of non-superuser profiles.

  - **Methods:**
    - GET: Retrieve the list of non-superuser profiles.

  - **Response:**
    - **Success (200 OK):** Returns a list of non-superuser profiles.
      ```json
      [
        {
          "id": 3,
          "username": "non_superuser1@example.com",
          "email": "non_superuser1@example.com"
          // ... other user fields
        },
        {
          "id": 4,
          "username": "non_superuser2@example.com",
          "email": "non_superuser2@example.com"
          // ... other user fields
        }
        // ... other non-superuser profiles
      ]
      ```

### Activate/Deactivate User API

- **Description:** Activate or deactivate a user based on the provided user_id.

  - **Methods:**
    - PUT: Activate or deactivate a user.

  - **Request Body:**
    ```json
    {
      "is_active": true
    }
    ```

  - **Response:**
    - **Success (200 OK):** Returns the updated user details.
      ```json
      {
        "id": 3,
        "username": "non_superuser1@example.com",
        "email": "non_superuser1@example.com",
        "is_active": true
        // ... other user fields
      }
      ```
    - **Error (4xx):** If the user is not found, an appropriate error response is returned.
      ```json
      {
        "message": "User not found"
      }
      ```

### Change Password API

- **Description:** Change the password for the authenticated user.

  - **Methods:**
    - PUT: Change the password for the authenticated user.

  - **Request Body:**
    ```json
    {
      "old_password": "current_password",
      "new_password": "new_password"
    }
    ```

  - **Response:**
    - **Success (200 OK):** Password changed successfully.
      ```json
      {
        "detail": "Password changed successfully."
      }
      ```
    - **Error (4xx):** If the old password is incorrect, an appropriate error response is returned.
      ```json
      {
        "detail": "Old password is incorrect."
      }
      ```

### Update Mobile API

- **Description:** Update the mobile number of the specified user.

  - **Methods:**
    - PUT: Update the mobile number of the specified user.

  - **Request Body:**
    ```json
    {
      "mobile": "new_mobile_number"
    }
    ```

  - **Response:**
    - **Success (200 OK):** Returns the updated user details.
      ```json
      {
        "id": 2,
        "username": "user@example.com",
        "email": "user@example.com",
        "mobile": "new_mobile_number"
        // ... other user fields
      }
      ```
    - **Error (4xx):** If the user does not have permission, an appropriate error response is returned.
      ```json
      {
        "detail": "You do not have permission to perform this action."
      }
      ```

## Restaurant API
### Create Restaurant API

- **Endpoint:** `/add-restorant/`
- **Method:** POST
- **Description:** Create a new restaurant.
  
  - **Request JSON Format:**
    ```json
    {
      "name": "Restaurant Name",
      "address": "Restaurant Address",
      "contact_info": "Contact Information",
      "logo_url": "URL to Restaurant Logo",
      "url": "Restaurant Website URL"
    }
    ```

  - **Response:**
    - **Status (201 Created):** Restaurant creation successful. Returns the newly created restaurant details.
      ```json
      {
        "id": 1,
        "name": "Restaurant Name",
        "address": "Restaurant Address",
        "contact_info": "Contact Information",
        "logo_url": "URL to Restaurant Logo",
        "url": "Restaurant Website URL"
      }
      ```

### Update Restaurant API

- **Endpoint:** `/update-restorant/<int:pk>/`
- **Methods:** GET, PUT, DELETE
- **Description:**
  - **GET:** Retrieve details of a specific restaurant.
  - **PUT:** Update details of a specific restaurant.
  - **DELETE:** Delete a specific restaurant.
  
  - **Request JSON Format (for PUT):**
    ```json
    {
      "name": "Updated Restaurant Name",
      "address": "Updated Restaurant Address",
      "contact_info": "Updated Contact Information",
      "logo_url": "Updated URL to Restaurant Logo",
      "url": "Updated Restaurant Website URL"
    }
    ```

  - **Response (for GET):**
    - **Status (200 OK):** Returns details of the specific restaurant.
      ```json
      {
        "id": 1,
        "name": "Updated Restaurant Name",
        "address": "Updated Restaurant Address",
        "contact_info": "Updated Contact Information",
        "logo_url": "Updated URL to Restaurant Logo",
        "url": "Updated Restaurant Website URL"
      }
      ```

  - **Response (for PUT):**
    - **Status (200 OK):** Returns the updated details of the specific restaurant.
      ```json
      {
        "id": 1,
        "name": "Updated Restaurant Name",
        "address": "Updated Restaurant Address",
        "contact_info": "Updated Contact Information",
        "logo_url": "Updated URL to Restaurant Logo",
        "url": "Updated Restaurant Website URL"
      }
      ```

  - **Response (for DELETE):**
    - **Status (204 No Content):** Restaurant deletion successful.

## Menus

### List/Create Menus
- **Method:** GET (List), POST (Create)
- **Endpoint:** `/menus/`

  **Request JSON (POST):**
  ```json
  {
    "restaurant_id": 1,
    "title": "New Menu",
    "description": "Menu description"
  }


---

## Contact and Contributors

For inquiries, support, or contributions, feel free to reach out to:

- Project Lead: [Leader Content here]
- Developers: 

### Important Links
- [Link1]
- [Link2]

## License

[License information]

---

Thank you for using QR Menu SAAS! We appreciate your support.
