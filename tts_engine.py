import asyncio
import edge_tts
import os
import uuid
from playsound import playsound
import re

VOICE = "en-IN-PrabhatNeural"
RATE = "+25%"
PITCH = "-6Hz"

def clean_text(text: str) -> str:
    # Remove markdown, symbols, bullets
    text = re.sub(r"[*_#`•>-]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

async def _speak(text):
    filename = f"tts_{uuid.uuid4()}.mp3"
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate=RATE,
        pitch=PITCH
    )
    await communicate.save(filename)
    playsound(filename)
    os.remove(filename)

def speak(text: str):
    text = clean_text(text)
    if not text:
        return
    asyncio.run(_speak(text))
