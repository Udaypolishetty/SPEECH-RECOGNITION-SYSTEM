# 🗣️ Speech-to-Text and Short Audio Transcriber

This project is a **Speech-to-Text Application** built using **Gradio**, **SpeechRecognition**, and **pydub**. It allows users to either upload short audio files or record live audio from their microphone and get real-time transcriptions.

## ✨ Features

- Upload audio files (`.mp3`, `.flac`, `.ogg`, etc.) for transcription
- Record live audio directly from microphone
- Transcribes using Google's Speech Recognition API
- Supports audio conversion using `pydub` and `ffmpeg`
- Simple and clean Gradio-based web interface

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install gradio SpeechRecognition pydub
   ```

2. Download and install [FFmpeg](https://ffmpeg.org/download.html), and set the correct path for `ffmpeg.exe` and `ffprobe.exe` in your code:
   ```python
   FFMPEG_PATH = r"C:\path\to\ffmpeg.exe"
   FFPROBE_PATH = r"C:\path\to\ffprobe.exe"
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. The app will launch in your browser at `http://127.0.0.1:7860/`.

## 🛠 Technologies Used

- Python
- Gradio
- SpeechRecognition
- Pydub
- FFmpeg

## 📌 Use Cases

- Quick transcription of meetings, lectures, or recordings
- Live speech-to-text functionality for short messages or captions
- Language accessibility tools

## 🙌 Credits

- Speech recognition via [Google Web Speech API](https://cloud.google.com/speech-to-text)
- UI: [Gradio](https://gradio.app)
- Developer: Uday

---

> 🔗 You are welcome to fork and customize this project for your own audio transcription tasks!
