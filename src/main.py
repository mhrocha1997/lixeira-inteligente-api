from fastapi import FastAPI

import models

# from .database import engine

app = FastAPI()

@app.get("/")
def test():
    return {"message": "OK"}