# creating a rest api
# create 4 endpoints
# GET /health (checks if an api is running or not)
# GET /requests (return all requests)
# POST /requests (creates requests)
# GET /requests/{req_id} (returns one request by ID)


from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(title="Flowpilot API")

# Data the client must provide when creating a request
class RequestCreate(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr
    message: str = Field(min_length=1)


# Data returned to the client, including the generated ID
class RequestItem(RequestCreate):
    id: int


# Temporary in-memory storage
requests_db: dict[int, RequestItem] = {}
next_id = 1


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/requests", response_model=list[RequestItem])
def get_requests(
    limit: int = Query(default=10, ge=1, le=100)
):
    return list(requests_db.values())[:limit]


@app.post(
    "/requests",
    response_model=RequestItem,
    status_code=status.HTTP_201_CREATED,
)
def create_request(request: RequestCreate):
    global next_id

    new_request = RequestItem(
        id=next_id,
        name=request.name,
        email=request.email,
        message=request.message,
    )

    requests_db[next_id] = new_request
    next_id += 1

    return new_request


@app.get("/requests/{request_id}", response_model=RequestItem)
def get_request(request_id: int):
    request = requests_db.get(request_id)

    if request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Request not found",
        )

    return request