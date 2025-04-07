# 🎙️ AI Voice Assistant

A local, privacy-focused voice assistant that uses open-source LLMs (e.g., Mistral, TinyLlama) for intelligent responses. Built using **Streamlit**, **SpeechRecognition**, **Text-to-Speech**, and **ctransformers** to support offline chat and voice interaction.

---

## ✨ Features

- 🗣️ Voice command recognition using `speech_recognition`
- 💬 Text fallback for chat input
- 🎧 Voice output using `pyttsx3`
- 🤖 Local LLM-powered responses via `ctransformers`
- 🧠 Offline, private, and fast
- 💾 Chat history saved to a local file (`chat_history.txt`)

---
## 🚀 Getting Started

### Clone the Repo

```
git clone https://github.com/JagadeeshAjjada/AI_voice_assistant.git
```
```
cd AI_voice_assistant
```

```
pip install -r requirements.txt
```

### Install Dependencies

```
pip install -r requirements.txt
```

### 🧠 Run the Assistant

```
streamlit run app.py
```

---

### 🛠 Dependencies

- streamlit
- ctransformers
- pyttsx3
- speechrecognition
- pyaudio (for microphone input)
- openai-whisper (optional if adding transcription)
- transformers (optional if you switch back)
