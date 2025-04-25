# Friend – Voice Chatbot with Local and Cloud LLM Support

Friend is a voice-based chatbot that converts speech to text, generates responses using either a local LLM or Groq’s API, and then speaks the responses back. It’s designed as a self-contained loop for real-time, private voice interaction.

## Features

- Speech Recognition – Converts voice input into text using Google's Speech Recognition API.
- LLM Integration – Uses either:
  - A local LLM, if available
  - Or falls back to Groq API for remote LLM access automatically if the API key is configured
- Conversation History – Maintains a simple text-based memory between turns.
- Text-to-Speech (TTS) – Reads responses aloud using edge-tts and pydub.

## Usage

### Installation

Install dependencies from the included `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file with your Groq API key:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### LLM Setup (Local Use)

- You need to install Ollama from: https://ollama.com/download
- Run the following to pull the model used:

```bash
ollama pull llama3.2:3b
```

- You can explore other llama3.2 versions at: https://ollama.com/library/llama3.2:3b
- Or browse all available models here: https://ollama.com/search

> Note: The LLM was not prompted or fine-tuned in this project.

## Running the App

### Python Version

This code was tested under Python 3.8.5.

### Option 1: Python Script

Start the chatbot by running:

```bash
python main.py
```

The loop will:
- Wait for voice input (with timeout)
- Transcribe speech to text
- Generate a response (local or remote LLM)
- Speak the reply using TTS
- Repeat

If input is not recognized, the bot prompts via text to retry.

### Option 2: Jupyter Notebook

Use `main.ipynb` to test components separately:
- Speech recognition
- Chatbot logic
- TTS playback

## .gitignore Highlights

The project ignores:
- Virtual environments
- API keys
- History files
- Local notebooks for testing

## License

Licensed under the MIT License.