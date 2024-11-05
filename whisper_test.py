import whisper
import warnings

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

# Load the Whisper model
model = whisper.load_model("base") #base, #turbo, #tini, #small, and #large (more support models)

# Transcribe an audio file (replace 'your_audio_file.mp3' with your actual file path)
result = model.transcribe("Test.mp3")

# Print the transcription
print("Transcription:", result['text'])
