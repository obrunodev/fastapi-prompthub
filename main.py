from fastapi import FastAPI

app = FastAPI()


@app.get("/health-check")
def hello_world():
    return {"message": "Hello World"}
