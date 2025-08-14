from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    firstname: str
    lastname: str
    phone_number: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2 replacement for orm_mode
