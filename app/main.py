from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.models.prompt import PromptRequest, GenerateResponse

from app.services.game_generator import generate_game_from_prompt

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def home():
    return {"message" : "Welcome to AI Game Generator"}

@app.get("/app")
def frontend():
    return FileResponse("app/static/index.html")

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
    try:
        generated_game = generate_game_from_prompt(request.prompt)

        return {
            "game_html" : generated_game,
            "prompt": request.prompt,
            "status" : "completed"
        }

    except Exception as error:
        raise HTTPException(
            status_code = 500,
            detail = f"Game generation failed: {str(error)}"
        ) 
