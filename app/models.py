from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import datetime

class RequestCreate(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr
    message: str = Field(min_length=1)

class RequestItem(RequestCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    status: str = "open"
    created_at: datetime

class RequestResponse(RequestItem):
    pass

class Request(Base):
    __tablename__ = "requests"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    message: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String, default="open")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
