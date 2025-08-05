# backend/app/schemas/user_schema.py

from pydantic import BaseModel, EmailStr

# Used when a new user is being created (input schema)
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Used to return user info in responses (output schema)
class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True