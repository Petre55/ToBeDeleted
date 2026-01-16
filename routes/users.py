from fastapi import APIRouter, HTTPException
from typing import List

from models.user import User, User_Response


router = APIRouter()

# Sample data store
users_db: List[User] = [
    User(id=1, username="john_doe", email="john@example.com", full_name="John Doe"),
    User(id=2, username="jane_smith", email="jane@example.com", full_name="Jane Smith"),
]


@router.get("/", response_model=List[User_Response])
def get_users():
    """Return all users."""
    return users_db


@router.post("/", response_model=User_Response)
def create_user(user: User):
    """Create a new user. Returns 400 if the id already exists."""
    for existing_user in users_db:
        if existing_user.id == user.id:
            raise HTTPException(status_code=400, detail="User with this id already exists")
    users_db.append(user)
    return user


@router.get("/{id}", response_model=User)
def get_user(id: int):
    """Return a full user by ID or raise 404."""
    for user in users_db:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{id}")
def delete_user(id: int):
    """Remove user by ID or raise 404."""
    for index, user in enumerate(users_db):
        if user.id == id:
            del users_db[index]
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")