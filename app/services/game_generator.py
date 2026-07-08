from app.services.prompt_builder import build_game_prompt

def generate_game_from_prompt(prompt: str):
    ai_prompt = build_game_prompt(prompt)
    return ai_prompt