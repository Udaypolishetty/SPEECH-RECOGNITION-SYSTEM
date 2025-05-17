# SPEECH-RECOGNITION-SYSTEM

COMPANY: CODETECH IT SOLUTIONS

NAME: POLISHETTY UDAY

INTERN ID: CODF47

DOMAIN: Web-based AI and Speech Recognition

DURATION: 4-WEEKS

MENTOR: NEELA SANTOSH

#DESCRIPTION:

THIS PROJECT IS A USER-FRIENDLY SPEECH-TO-TEXT APPLICATION BUILT WITH PYTHON AND THE GRADIO LIBRARY FOR CREATING AN INTERACTIVE WEB INTERFACE. IT ALLOWS USERS TO TRANSCRIBE AUDIO FROM UPLOADED FILES OR RECORDED LIVE FROM THEIR MICROPHONE.

THE APPLICATION UTILIZES SEVERAL KEY PYTHON LIBRARIES:

* **`os`**: For interacting with the operating system, primarily used here to manage file paths and remove temporary converted audio files.
* **`gradio as gr`**: For creating the interactive web interface with simple Python code, providing an easy way for users to interact with the speech-to-text functionality.
* **`speech_recognition as sr`**: This crucial library provides the tools for performing speech recognition, supporting various engines, including the Google Speech Recognition API used in this project.
* **`pydub`**: This library is used for working with audio files, specifically to handle different audio formats like MP3, FLAC, and OGG. It's used to convert these formats to WAV, which is more readily processed by the `speech_recognition` library.

THE CODE DEFINES TWO MAIN FUNCTIONS FOR TRANSCRIPTION:

* **`transcribe_audio_file(file)`**: This function takes the path of an uploaded audio file as input. It first checks the file format. If it's MP3, FLAC, or OGG, it uses `pydub` to convert it to a WAV file. Then, it uses the `speech_recognition` library to open the audio file, record the audio data, and transcribe it using the Google Speech Recognition API. Finally, it removes the temporary WAV file (if created) and returns the transcribed text. It includes error handling for cases where the audio is unintelligible, there's an issue with the Google API, or other exceptions occur.
* **`transcribe_live_microphone()`**: This function uses the `speech_recognition` library to access the user's microphone. It adjusts the recognizer for ambient noise and then listens for audio input. Once audio is captured, it uses the Google Speech Recognition API to transcribe it and returns the resulting text. It also includes error handling for similar issues as the file transcription function.

THE USER INTERFACE IS BUILT USING GRADIO'S `Blocks` API, organized into two tabs:

* **"🎧 Upload Audio File"**: This tab provides an `Audio` component for users to upload audio files. A `Textbox` is displayed to show the transcribed text after the user clicks the "Transcribe Audio File" button. The button triggers the `transcribe_audio_file` function.
* **"🎤 Record Live from Microphone"**: This tab features a `Textbox` that serves as a placeholder and displays the live transcribed text. A "Record🔴 and Transcribe ၊၊||၊" button initiates the live recording and transcription process using the `transcribe_live_microphone` function, with the output displayed in the `Textbox`.

THE APPLICATION ALSO SETS UP THE PATHS FOR `ffmpeg` and `ffprobe`, which are external tools required by `pydub` to handle various audio formats. It adds the directory containing these executables to the system's PATH environment variable and explicitly sets the converter and ffprobe paths for `AudioSegment`.

THIS PROJECT PROVIDES A CONVENIENT WAY TO PERFORM SPEECH-TO-TEXT TRANSLATION FOR BOTH EXISTING AUDIO FILES AND LIVE RECORDINGS, LEVERAGING THE POWER OF THE GOOGLE SPEECH RECOGNITION API AND A SIMPLE YET EFFECTIVE WEB INTERFACE CREATED WITH GRADIO. IT DEMONSTRATES SKILLS IN AUDIO PROCESSING, SPEECH RECOGNITION API INTEGRATION, AND WEB INTERFACE DEVELOPMENT USING PYTHON LIBRARIES.

# SAMPLE OUTPUT:
