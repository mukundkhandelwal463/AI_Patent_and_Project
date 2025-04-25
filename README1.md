🤖 Voice-Controlled AI Assistant using Google Gemini
📌 Project Title:
"Jarvis" – A Voice Assistant with Google Gemini AI Integration

👨‍💻 Developed By:
Mukund Khandelwal
Email: mukundkhandelwal463@gamil.com
University: Lovely Professional University, Punjab, India

🧠 Project Overview
This Python-based AI voice assistant, nicknamed Jarvis, listens for your voice, responds using speech synthesis, and can answer questions or execute commands using the Google Gemini API. It supports basic voice commands like opening websites, playing songs, fetching news, and holding natural conversations.

🎯 Objectives
Build a personalized and interactive AI voice assistant.

Integrate Google Gemini (Generative AI) for intelligent Q&A.

Perform system actions via voice, like opening websites and media content.

🧩 Key Features
🔊 Voice Activation via wake word: “Jarvis”

🌐 Gemini AI integration for Q&A and conversational support

🗣️ Text-to-Speech (TTS) responses using pyttsx3

🧏‍♂️ Speech Recognition via speech_recognition

🔗 Open favorite websites or media via voice commands

🎶 Supports playing songs and news directly from web links

✅ Graceful exit on saying "exit", "quit", or "stop"

🛠️ Technologies Used

Module	Purpose
speech_recognition	Capture and interpret voice input
pyttsx3	Text-to-speech for voice feedback
webbrowser	Open URLs in default browser
dotenv	Secure API key storage (optional)
google.generativeai	Google Gemini API integration
🔧 Setup Instructions
Install Required Libraries:

bash
Copy
Edit
pip install SpeechRecognition pyttsx3 python-dotenv google-generativeai
Environment Configuration:

(Optional) Create a .env file to store your API key securely.

Add:

ini
Copy
Edit
GOOGLE_API_KEY=your_gemini_api_key_here
Run the Assistant:

bash
Copy
Edit
python your_script.py
Speak "Jarvis" to activate the assistant, then give your command.

🚀 Sample Voice Commands
“Open Google”

“Play my favourite song”

“Open today news”

“What is quantum computing?”

“Stop” or “Exit” to quit

🔐 Security Note
API keys are currently hardcoded. It’s strongly advised to move them to a .env file and load them securely using dotenv.

💡 Future Improvements
Add support for custom wake words

Extend functionality with home automation features

Add multi-language support

Enhance error handling and command learning

📎 Keywords
Voice Assistant, Google Gemini API, Python Speech Recognition, pyttsx3, AI Voice Control, Jarvis, AI Q&A, Wake Word Detection
