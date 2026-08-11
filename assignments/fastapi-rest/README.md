# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using the FastAPI framework by defining routes, request and response models, and handling data validation.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description

Build a FastAPI application that manages a collection of items through standard REST endpoints.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Include routes for `GET /items`, `GET /items/{item_id}`, `POST /items`, `PUT /items/{item_id}`, and `DELETE /items/{item_id}`
- Return JSON responses for all endpoints
- Use appropriate HTTP status codes for success and error cases

### 🛠️ Define Pydantic Models and Validation

#### Description

Add Pydantic models to validate request data and shape API responses.

#### Requirements
Completed program should:

- Define request models such as `ItemCreate` and `ItemUpdate`
- Define a response model such as `Item`
- Validate that `name` is a non-empty string and `price` is a positive number
- Accept an optional `description` field
- Return validation errors automatically for invalid data

### 🛠️ Implement In-Memory Data Storage

#### Description

Use a simple in-memory storage mechanism to support item creation, retrieval, updating, and deletion.

#### Requirements
Completed program should:

- Store items in a Python dictionary or list with unique IDs
- Assign incremental or UUID-based IDs when creating new items
- Update existing items when `PUT /items/{item_id}` is called
- Delete items when `DELETE /items/{item_id}` is called
- Return a 404 response if an item is not found
