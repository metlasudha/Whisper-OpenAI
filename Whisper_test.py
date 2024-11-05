
Automatically Speech / Audio to Text converter
==============================================

Python installation 

PyCharm IDE installation 

=====================

Pytourch and whisper packages installation 

pip install openai-whisper torch

=================

ffmpeg module installation

----------------------------------------------------
Fixing the FileNotFoundError for ffmpeg

Step 1: Install ffmpeg
Download ffmpeg from FFmpeg's official website.  https://ffmpeg.org/download.html
Unzip the downloaded file, and note the location where you extract the folder.
Step 2: Add ffmpeg to System Path

Open Settings:
On Windows, search for “Environment Variables” in the start menu and open the Environment Variables dialog.
Under System Variables, find the Path variable and edit it.
Add the path to the bin folder inside your ffmpeg folder (e.g., C:\ffmpeg\bin).
Click OK to save the changes.
Step 3: Restart PyCharm
After updating the environment variables, restart PyCharm to ensure it picks up the new system path.
Step 4: Re-run the Program
After setting up ffmpeg correctly, try running your program again. The Whisper model should now be able to access ffmpeg and process the audio file.

=========================

Create a python file

whisper_test.py

===================


import whisper
import warnings

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe an audio file (replace 'your_audio_file.mp3' with your actual file path)
result = model.transcribe("Test.mp3")

# Print the transcription
print("Transcription:", result['text'])


=========================

If you feel this content is useful subscribe channel for more videos

Thanks

Harisystems.com
info@harisystems.com
