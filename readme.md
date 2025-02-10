# Friend Project

This project is a voice-based chatbot that uses speech recognition to convert voice input to text, interacts with a Groq-based chatbot to generate responses, and converts the responses back to speech for playback. The main script integrates these functionalities into a continuous loop for real-time interaction.

## Features
1. **Speech Recognition**: Converts voice input from the microphone to text.
2. **Chatbot Conversation**: Interacts with a Groq-based chatbot to generate responses.
3. **Text-to-Speech**: Converts the chatbot's text response back to speech and plays it.

## Requirements
The project requires the following Python packages:
- SpeechRecognition
- python-dotenv
- groq
- edge_tts
- pydub

These can be installed using the `requirements.txt` file:
```sh
pip install -r requirements.txt
```

## Usage
Speech Recognition
The recognize_speech_from_mic function converts audio from the microphone to text using the Google Speech Recognition API.

LLM Chatbot
The groq_chatbot_conversation function interacts with a Groq-based chatbot that maintains conversation context using a text file.

Text-to-Speech
The speak function converts text to speech and plays it using the edge_tts and pydub libraries.

Main Loop
The main loop combines the above functions to create a voice bot that listens to the user, generates a response, and speaks the response.

### Running the Project
1. Ensure you have all the required packages installed.
2. Run the `main.py` script:
```sh
python main.py
```

### Jupyter Notebook
The project also includes a Jupyter Notebook `main.ipynb` that demonstrates the individual components:
1. **Speech Recognition**: Functions to convert audio to text.
2. **Chatbot Conversation**: Function to maintain conversation context with the chatbot.
3. **Text-to-Speech**: Function to convert text to speech and play it.

## Environment Variables
The project uses environment variables for configuration. Create a `.env` file in the project root with the following content:
```
GROQ_API_KEY=your_groq_api_key_here
```

## .gitignore
The `.gitignore` file includes:
- `venv`
- `.env`
- `*_history.txt`
- `test.ipynb`

## License
This project is licensed under the MIT License.
