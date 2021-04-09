from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test():
    return {"message": "OK"}