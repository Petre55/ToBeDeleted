# FastAPI Application

A modular FastAPI application with user and item management endpoints.

## Features

- **Users API**: Full CRUD operations for user management
- **Items API**: Read operations for item management
- **Modular Architecture**: Routes organized in separate files
- **Interactive Documentation**: Auto-generated Swagger UI

## Project Structure

```
├── main.py              # FastAPI application entry point
├── config.py            # Configuration file
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
├── README.md           # This file
├── models/
│   ├── item.py         # Item Pydantic models
│   └── user.py         # User Pydantic models
└── routes/
    ├── items.py        # Items routes
    └── users.py        # Users routes
```

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the server with hot reload:
```bash
uvicorn main:app --reload
```

The application will be available at:
- **Base URL**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Root
- `GET /` - Welcome message

### Users
- `GET /users/` - Get all users
- `POST /users/` - Create a new user
- `GET /users/{id}` - Get user by ID
- `DELETE /users/{id}` - Delete user by ID

### Items
- `GET /items/` - Get all items
- `GET /items/{id}` - Get item by ID

## Example Requests

### Get all users
```bash
curl http://localhost:8000/users/
```

### Create a user
```bash
curl -X POST http://localhost:8000/users/ \
  -H "Content-Type: application/json" \
  -d '{"id": 3, "username": "new_user", "email": "new@example.com", "full_name": "New User"}'
```

### Get item by ID
```bash
curl http://localhost:8000/items/1
```

## Dependencies

- fastapi>=0.100.0
- uvicorn>=0.23.0
- pydantic>=2.0.0
