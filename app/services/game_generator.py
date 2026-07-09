from app.services.prompt_builder import build_game_prompt
from app.services.gemini_client import generate_text
from app.services.fallback_game import build_fallback_game

def generate_game_from_prompt(prompt: str):
    ai_prompt = build_game_prompt(prompt)
    try:
        generated_game = generate_text(ai_prompt)
        return generated_game
    except Exception:
        return build_fallback_game(prompt)