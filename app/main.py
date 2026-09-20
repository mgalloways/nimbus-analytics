from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class StatusResponse(BaseModel):
    message: str

class DataRequest(BaseModel):
    name: str
    value: float

class DataResponse(BaseModel):
    name: str
    value: float

@app.get("/", response_model=StatusResponse)
def read_root():
    return {"message": "Nimbus Analytics is running!"}

@app.post("/data", response_model=DataResponse)
def receive_data(data: DataRequest):
    return {
        "name": data.name,
        "value": data.value
    }