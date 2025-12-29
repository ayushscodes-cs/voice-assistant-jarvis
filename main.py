import speech_recognition as sr
import webbrowser
from tts_engine import speak
import youtube_search
import gemini_chat
import time
import conversation_memory




r = sr.Recognizer()

# -------- Session State --------
session_active = False
SESSION_TIMEOUT = 20   # seconds
last_active_time = 0
conversation_active = False

# -------------------------------


def is_simple_command(c):
    keywords = [
        "open", "play", "google", "youtube",
        "instagram", "whatsapp", "gmail"
    ]
    return any(k in c for k in keywords)

   
       
def processCommand(c):
    c = c.lower().strip()


    if "open google" in c:
        webbrowser.open("https://www.google.com/")
        return
    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com/")
        return
    elif "open instagram" in c:
        webbrowser.open("https://www.instagram.com/")
        return
    elif "open whatsapp" in c:
        webbrowser.open("https://www.whatsapp.com/")
        return
    elif "open gmail" in c:
        webbrowser.open("https://mail.google.com/")
        return
    elif "open chat gpt" in c:
        webbrowser.open("https://www.chatgpt.com/")
        return
    
    elif c.startswith("play "):
        search = c.replace("play", "").strip()
        speak(f"Playing {search}")
        URL = youtube_search.search_youtube(search)
        if URL:
            webbrowser.open(URL)
        else:
            speak("Sorry, I could not find it!")
            return
    
    elif not is_simple_command(c):
        global last_active_time
        print("Thinking")
        conversation_memory.add_user(c)
        prompt = conversation_memory.build_prompt()
        reply = gemini_chat.chat_with_gemini(prompt)
        print("Jarvis:", reply)
        speak(reply)
        conversation_memory.add_jarvis(reply)
        last_active_time = time.time()  
        return 
    

    else:
        speak("Command not recognized")
        print("Command:", c)

if __name__ == "__main__":

    # Mic calibration ONCE
    with sr.Microphone() as source:
        print("Calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=1)

    
    
    

    while True:
        try:
            
            with sr.Microphone() as source:
                print("\n🎧 Listening...")
                audio = r.listen(source)

            text = r.recognize_google(audio).lower().strip()
            print("✅ Heard:", repr(text))

            current_time = time.time()

            #  SESSION TIMEOUT CHECK
            if conversation_active and (current_time - last_active_time > SESSION_TIMEOUT):
                conversation_active = False
                session_active = False
                
                print("🛑 Session ended due to timeout")
                continue

            #  WAKE WORD DETECTED
            if "jarvis" in text:
                command = text.replace("jarvis", "").strip()
                conversation_active = True
                session_active = True
                
                last_active_time = current_time

                # Case 1: only "jarvis"
                if not command:
                    speak("yes...")
                    continue

                # Case 2: "jarvis + command"
                processCommand(command)
                continue

            #  FOLLOW-UP WITHOUT WAKE WORD
            if conversation_active:
                last_active_time = current_time

                # stop always works
                if "stop" in text:
                    speak("Okay")
                    conversation_active = False
                    session_active = False
                    continue
                elif "quit" in text or "quit" in text or "terminate" in text:
                    speak("Okay")
                    conversation_active = False
                    session_active = False
                    break   

                # follow-up like "elaborate more"
                processCommand(text)
                continue

            #  IGNORE EVERYTHING ELSE
            print("⏭️ Ignored (no wake word)")

        except sr.UnknownValueError:
            print("❌ Could not understand")
        except Exception as e:
            print("⚠️ Error:", e)