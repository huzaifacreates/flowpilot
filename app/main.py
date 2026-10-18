# creating a rest api
# create 4 endpoints
# GET /health (checks if an api is running or not)
# GET /requests (return all requests)
# POST /requests (creates requests)
# GET /requests/{req_id} (returns one request by ID)


from app.database import Base, engine, get_db
from sqlalchemy.orm import Session
from app import models
from fastapi import Depends, FastAPI, HTTPException, Query, status
from app.models import RequestCreate, RequestResponse



app = FastAPI(title="Flowpilot API")
Base.metadata.create_all(bind=engine)

# Temporary in-memory storage
# requests_db: dict[int, RequestItem] = {}
# next_id = 1


# endpoint 1
@app.get("/health")
def health_check():
    return {"status": "healthy"}


# endpoint 2
@app.get("/requests", response_model=list[RequestResponse])
def get_requests(
    db: Session = Depends(get_db),
    limit: int = Query(default=10, ge=1, le=100)
):
    return db.query(models.Request).limit(limit).all()


# endpoint 3
@app.post(
    "/requests",
    response_model=RequestResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_request(request: RequestCreate, db: Session = Depends(get_db)):
    new_request = models.Request(**request.model_dump())

    db.add(new_request)
    db.commit()
    db.refresh(new_request)

    return new_request


# endpoint 4
@app.get("/requests/{request_id}", response_model=RequestResponse)
def get_request(request_id: int, db: Session = Depends(get_db)):
    request = db.get(models.Request, request_id)

    if request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Request not found",
        )

    return request




# endpoint 5
@app.delete("/requests/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_request(request_id: int, db: Session = Depends(get_db)):
    request = db.get(models.Request, request_id)

    if request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="request not found"
        )

    db.delete(request)
    db.commit()
    return None
