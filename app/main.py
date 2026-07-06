from fastapi import FastAPI

from app.models.prompt import PromptRequest, GenerateResponse


app = FastAPI()


@app.get("/")
def home():
    return {"message" : "Welcome to AI Game Generator"}


@app.get("/hello/{name}")
def hello(name : str):
    return {"message" : f"Hello {name}!"}


@app.get("/about")
def about():
    return {"project" : "AI Game Generator"}


@app.get("/creator")
def creator():
    return {"creator" : "Aadi Tiwari"}


@app.post("/generate", response_model= GenerateResponse)
def generate_game(request: PromptRequest):
    return {
        "message" : "Game Generation request received",
        "prompt": request.prompt,
        "status" : "pending"
    }
