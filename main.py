from fastapi import FastAPI
from app.users.routes import router as user_router

app = FastAPI()


@app.get("/health-check")
def hello_world():
    return {"message": "Hello World"}


app.include_router(user_router, prefix="/users")
