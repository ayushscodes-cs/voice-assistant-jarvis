from google import genai
import os

# Configure client with API key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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
