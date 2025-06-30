import pyaudio
import wave
import time
import os
from datetime import datetime

# Banner
print("""
███╗   ███╗██╗ ██████╗███████╗██████╗ ██╗   ██╗██████╗  ██████╗ ████████╗
████╗ ████║██║██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗██╔═══██╗╚══██╔══╝
██╔████╔██║██║██║     ███████╗██████╔╝ ╚████╔╝ ██████╔╝██║   ██║   ██║   
██║╚██╔╝██║██║██║     ╚════██║██╔═══╝   ╚██╔╝  ██╔══██╗██║   ██║   ██║   
██║ ╚═╝ ██║██║╚██████╗███████║██║        ██║   ██████╔╝╚██████╔╝   ██║   
╚═╝     ╚═╝╚═╝ ╚═════╝╚══════╝╚═╝        ╚═╝   ╚═════╝  ╚═════╝    ╚═╝   
                                                                         
Coded by Pakistani Ethical Hacker: Mr. Sabaz Ali Khan
""")

def record_audio(duration=5, output_filename=None):
    """
    Record audio from microphone for a specified duration and save to a WAV file.
    
    Parameters:
    - duration: Length of recording in seconds (default: 5)
    - output_filename: Name of the output WAV file (default: timestamped filename)
    """
    # Audio settings
    FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
    CHANNELS = 1              # Mono audio
    RATE = 44100              # Sample rate (Hz)
    CHUNK = 1024              # Buffer size

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Create output filename with timestamp if none provided
    if output_filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"recording_{timestamp}.wav"

    # Open stream
    stream = audio.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=RATE,
                       input=True,
                       frames_per_buffer=CHUNK)

    print(f"Recording for {duration} seconds...")

    # Record audio
    frames = []
    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording finished.")

    # Stop and close stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save to WAV file
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved as {output_filename}")

def main():
    try:
        # Get user input for recording duration
        duration = int(input("Enter recording duration in seconds (default 5): ") or 5)
        output_filename = input("Enter output filename (press Enter for default): ").strip() or None

        # Validate duration
        if duration <= 0:
            print("Duration must be positive.")
            return

        # Record audio
        record_audio(duration, output_filename)

    except ValueError:
        print("Invalid input. Please enter a valid number for duration.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()