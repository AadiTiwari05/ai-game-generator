def build_fallback_game(user_prompt: str):
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Fallback Game</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            background: #f4f4f4;
            padding: 40px;
        }}

        #gameBox {{
            margin: 20px auto;
            padding: 30px;
            width: 300px;
            background: white;
            border: 2px solid #333;
        }}

        button {{
            padding: 12px 20px;
            font-size: 16px;
            cursor: pointer;
        }}

        #score {{
            font-size: 24px;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1>Mini Click Game</h1>
    <p>Your requested game was: {user_prompt}</p>

    <div id="gameBox">
        <p>Click the button to score points!</p>
        <p>Score: <span id="score">0</span></p>
        <button onclick="increaseScore()">Click Me</button>
    </div>

    <script>
        let score = 0;

        function increaseScore() {{
            score += 1;
            document.getElementById("score").textContent = score;
        }}
    </script>
</body>
</html>
"""