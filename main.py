import speech_recognition as sr
from groq import Groq
import ollama
import os
import json
from dotenv import load_dotenv

import asyncio
import edge_tts
import io
from pydub import AudioSegment
from pydub.playback import play

# Load environment variables
load_dotenv()

r = sr.Recognizer()

def recognize_speech_from_mic(recognizer):
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio_text = r.listen(source)
    print("Recognizing...")
        
    try:
        return r.recognize_google(audio_text)
    except:
        print("Could not recognize ...")
        return recognize_speech_from_mic(recognizer)

def converse(new_message, model="llama-3.1-8b-instant", api_key=None, history_file="conversation_history.txt"):
    """
    A function to interact with a Groq-based chatbot that maintains conversation context using a text file.

    Parameters:
    - new_message (str): The user's latest input message.
    - model (str): The model to use (default: "llama-3.1-8b-instant").
    - api_key (str): Groq API key (default: None, will use GROQ_API_KEY from environment variables if not provided).
    - history_file (str): The file to store conversation history (default: "conversation_history.txt").

    Returns:
    - str: The chatbot's response.
    """

    # Load conversation history
    if os.path.exists(history_file):
        with open(history_file, "r", encoding="utf-8") as file:
            messages = json.load(file)
    else:
        messages = []

    # Append new user message
    messages.append({"role": "user", "content": new_message})

    api_key = api_key or os.getenv("GROQ_API_KEY")

    if api_key:
        client = Groq()
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        response_text = ""
        for chunk in completion:
            response_text += chunk.choices[0].delta.content or ""

    else:
        response = ollama.chat(
        model="llama3.2:3b",
        messages=messages
        )
        response_text = response["message"]["content"]

    
    # Append assistant response
    messages.append({"role": "assistant", "content": response_text})
    
    # Save updated conversation history
    with open(history_file, "w", encoding="utf-8") as file:
        json.dump(messages, file, indent=4)
    
    return response_text

async def speak(text: str, voice="en-US-MichelleNeural", rate="+100%"):
    """Convert text to speech and play it."""
    tts = edge_tts.Communicate(text, voice, rate=rate)
    stream = io.BytesIO()

    async for chunk in tts.stream():
        if chunk["type"] == "audio":
            stream.write(chunk["data"])

    stream.seek(0)
    audio = AudioSegment.from_file(stream, format="mp3")
    play(audio)

async def main():
    while True:
        user_text = recognize_speech_from_mic(r)
        print("user: ", user_text)
        response = converse(user_text)
        print("bot: ", response)
        await speak(response, voice="en-US-MichelleNeural", rate="+20%")

if __name__ == "__main__":
    asyncio.run(main())
