from app.services.prompt_builder import build_game_prompt
from app.services.gemini_client import generate_text

def generate_game_from_prompt(prompt: str):
    ai_prompt = build_game_prompt(prompt)
    generated_game = generate_text(ai_prompt)

    return generated_game