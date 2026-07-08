def build_game_prompt(user_prompt: str):
    return f"""
You are an expert browser game developer.
Create a complete playable browser game based on this user request:
{user_prompt}

Requirements:
- Return one complete HTML file.
- Include all CSS inside a <style> tag.
- Include all JavaScript inside a <script> tag.
- Do not use external libraries.
- Do not include markdown formatting.
- Do not explain the code.
- The game should be playable immediately in a browser.
- The game must be safe for all ages.
- Do not include adult, sexual, graphic, hateful, or explicit content.
- Do not include gambling, real-money betting, or illegal activity.
- If the user requests unsafe or adult content, create a family-friendly alternative instead. 
"""