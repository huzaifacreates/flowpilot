from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class RequestCreate(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr
    message: str = Field(min_length=1)

class RequestItem(RequestCreate):
    id: int
    status: str = "open"
    created_at: datetime

class RequestResponse(RequestItem):
    pass