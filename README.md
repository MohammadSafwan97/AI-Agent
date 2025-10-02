Jarvis AI Agent 🎤🤖
====================

A simple voice-controlled AI assistant built with Python.  
Jarvis listens to your voice, responds intelligently using OpenAI’s GPT models, and speaks back.  

--------------------------------
✨ Features
--------------------------------
- Wake word detection ("Jarvis") to activate
- Voice-to-text (SpeechRecognition + Google Speech API)
- Natural responses powered by OpenAI GPT (via LiteLLM)
- Text-to-speech (pyttsx3)
- Conversation memory
- Activate/Deactivate by voice ("exit", "bye", "stop")

--------------------------------
🛠 Installation
--------------------------------
1. Clone this repository:
   git clone https://github.com/YOUR_USERNAME/jarvis-ai-agent.git
   cd jarvis-ai-agent

2. Install dependencies:
   pip install -r requirements.txt

Dependencies:
- litellm → connect to OpenAI API
- speechrecognition → microphone input
- pyttsx3 → text-to-speech
- pyaudio → microphone access

--------------------------------
🔑 API Key Setup
--------------------------------
Jarvis requires an OpenAI API key.

1. Go to https://platform.openai.com/account/api-keys and generate a key.
2. Save it in your environment variables:

Linux / macOS (bash/zsh):
   export OPENAI_API_KEY="your_api_key_here"

Windows (PowerShell):
   setx OPENAI_API_KEY "your_api_key_here"

Or use a `.env` file (recommended).

--------------------------------
▶️ Running Jarvis
--------------------------------
Start the agent with:
   python agent.py

Jarvis will:
- Start in inactive mode (just listening).
- Activate when you say "Jarvis".
- Ask “Yes? What can I do?” and wait for your command.
- Respond using AI and speak back.
- Deactivate when you say "exit", "bye", or "stop".

--------------------------------
📂 Project Structure
--------------------------------
jarvis-ai-agent/
│── agent.py         # Main AI agent
│── Listen.py        # Voice input (speech-to-text)
│── speak.py         # Voice output (text-to-speech)
│── requirements.txt # Python dependencies
│── README.txt       # Project documentation
│── .gitignore       # Ignore venv, .env, cache files

--------------------------------
🚀 Future Improvements
--------------------------------
- Hotword detection with better accuracy (using snowboy or whisper)
- GUI version
- Support for multiple voices
- Integration with external tools (e.g., open websites, system commands)

--------------------------------
📝 License
--------------------------------
MIT License.  
Feel free to use and modify this project.
