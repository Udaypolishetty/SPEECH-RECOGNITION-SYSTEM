import os
import gradio as gr
import speech_recognition as sr
from pydub import AudioSegment

# Set up ffmpeg path
FFMPEG_PATH = r"C:\Users\DELL\Downloads\bin\ffmpeg.exe"
FFPROBE_PATH = r"C:\Users\DELL\Downloads\bin\ffprobe.exe"

os.environ["PATH"] += os.pathsep + os.path.dirname(FFMPEG_PATH)
AudioSegment.converter = FFMPEG_PATH
AudioSegment.ffprobe = FFPROBE_PATH

recognizer = sr.Recognizer()

# Function to transcribe uploaded audio files
def transcribe_audio_file(file):
    try:
        audio_path = file
        if file.endswith(".mp3") or file.endswith(".flac") or file.endswith(".ogg"):
            sound = AudioSegment.from_file(file)
            audio_path = file.replace(".", "_converted.") + "wav"
            sound.export(audio_path, format="wav")

        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)

        if audio_path != file and os.path.exists(audio_path):
            os.remove(audio_path)

        return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"Google API Error: {e}"
    except Exception as e:
        return f"Error: {e}"

# Function to record live from microphone
def transcribe_live_microphone():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio_data = recognizer.listen(source)
            text = recognizer.recognize_google(audio_data)
            return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"Google API Error: {e}"
    except Exception as e:
        return f"Error: {e}"

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# 🗣️ Speech-to-Text and Short Audio Transcriber")

    with gr.Tab("🎧 Upload Audio File"):
        audio_input = gr.Audio(label="Upload Audio", type="filepath")
        output_text_file = gr.Textbox(label="Transcribed Text", lines=5)
        transcribe_button = gr.Button("Transcribe Audio File")
        transcribe_button.click(transcribe_audio_file, inputs=audio_input, outputs=output_text_file)

    with gr.Tab("🎤 Record Live from Microphone"):
        mic_output_text = gr.Textbox(placeholder = " Click below button to speak 👇 and speak without long gaps.....",label=" Live Transcribed Text", lines=5)
        mic_record_button = gr.Button("Record🔴 and Transcribe ၊၊||၊")
        mic_record_button.click(transcribe_live_microphone, outputs=mic_output_text)

demo.launch()
