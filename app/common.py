from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(title="FlowPilot API")

class RequestCreate(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr
    message: str = Field(min_length=1)

class RequestItem(RequestCreate):
    id: int


# endpoint 1
@app.get("/health")
def health_check():
    return {"status": "healthy"}
