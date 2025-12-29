from google import genai
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment

# Configure client with API key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found. Check .env file.")

client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
You are Jarvis, a voice assistant.
Rules:
- Keep answers SHORT (1–2 sentences max)
- Speak like a human assistant, not a teacher
- No bullet points
- No markdown
- No symbols
- No emojis
"""

def chat_with_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-robotics-er-1.5-preview",
        contents=[ SYSTEM_PROMPT, prompt ]
    )
    return response.text
