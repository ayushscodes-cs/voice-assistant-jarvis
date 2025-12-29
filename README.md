# Voice Assistant (Jarvis)

A Python-based voice assistant that uses speech recognition, text-to-speech, and an LLM to answer questions and execute commands.

## Features
- Wake word detection ("Jarvis")
- Session-based listening
- Conversational memory for follow-up questions
- Command handling (open apps, play YouTube, etc.)
- Text-to-speech using Microsoft Edge TTS

## Tech Stack
- Python
- SpeechRecognition
- Microsoft Edge TTS
- Gemini API

## What I Learned
- Managing session state in voice systems
- Why LLM APIs are stateless and how to design memory
- Debugging timing and OS-level audio issues
- Structuring a project into clean modules

## Limitations
- Microphone input is paused during speech to avoid audio conflicts on Windows
- Voice interrupt during speech is not supported on standard hardware

## Status
This is a learning project and my first step into building AI-powered assistants.
