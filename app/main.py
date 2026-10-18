# creating a rest api
# create 4 endpoints
# GET /health (checks if an api is running or not)
# GET /requests (return all requests)
# POST /requests (creates requests)
# GET /requests/{req_id} (returns one request by ID)


from app.database import Base, engine
from app import models
from fastapi import FastAPI, HTTPException, Query, status
from app.models import RequestCreate, RequestItem, RequestResponse
from datetime import datetime, timezone



app = FastAPI(title="Flowpilot API")
Base.metadata.create_all(bind=engine)

# Temporary in-memory storage
requests_db: dict[int, RequestItem] = {}
next_id = 1


# endpoint 1
@app.get("/health")
def health_check():
    return {"status": "healthy"}


# endpoint 2
@app.get("/requests", response_model=list[RequestItem])
def get_requests(
    limit: int = Query(default=10, ge=1, le=100)
):
    return list(requests_db.values())[:limit]


# endpoint 3
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
        created_at=datetime.now(timezone.utc)
    )

    requests_db[next_id] = new_request
    next_id += 1

    return new_request


# endpoint 4
@app.get("/requests/{request_id}", response_model=RequestItem)
def get_request(request_id: int):
    request = requests_db.get(request_id)

    if request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Request not found",
        )

    return request




# endpoint 5
@app.delete("/requests/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_request(request_id: int):
    if request_id not in requests_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="request not found"
        )

    del requests_db[request_id]
    return None
