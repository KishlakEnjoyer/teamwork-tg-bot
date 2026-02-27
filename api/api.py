from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/health")
def get_health():
    return {"status": "healthy"}
