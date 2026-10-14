from fastapi import FastAPI, Query, status, HTTPException
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


# temp db
temp_db: dict[int, RequestItem] = {}
next_id = 1


# endpoint 2
@app.get("/requests", response_model=list[RequestItem])
def get_requests(limit: int = Query(default=10, ge=1, le=100)):
    return list(temp_db.values())[:limit]



# endpoint 3
@app.post(
    "/requests",
    response_model=RequestItem,
    status_code=status.HTTP_201_exception
)
def create_request(request: RequestCreate):
    global next_id
    new_request = RequestItem(
        id = next_id,
        name = request.name,
        email = request.email,
        message = request.message
    )

    temp_db[next_id] = new_request
    next_id += 1

    return new_request