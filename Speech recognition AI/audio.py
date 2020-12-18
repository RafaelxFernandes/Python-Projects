import pyaudio
import wave
import speech_recognition
import subprocess
from commands import Commander

running = True
stop_commands = ["exit", "stop", "bye"]


def say(text):
    subprocess.call("say " + text, shell=True)


def play_audio(filename):
    chunk = 1024
    wave_file = wave.open(filename, "rb")
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format = pa.get_format_from_width(wave_file.getsampwidth()),
        channels = wave_file.getnchannels(),
        rate = wave_file.getframerate(),
        output = True
    )

    data_stream = wave_file.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wave_file.readframes(chunk)

    stream.close()
    pa.terminate()


recognizer = speech_recognition.Recognizer()
commander = Commander()


def init_speech():
    print("Wait for the beep...\n")
    play_audio("./audio/start.wav")

    with speech_recognition.Microphone() as source:
        print("Say something!")
        audio = recognizer.listen(source)

    play_audio("./audio/end.wav")

    command = ""

    try:
        print("Printing your command!")
        command = recognizer.recognize_google(audio)
        print("Your command: " + command + "\n")
        say("You said " + command)

        if(command in stop_commands):
            global running
            running = False
            say("Thanks for talking to me!")
        
        commander.discover(command)

    except:
        print("\nCouldn't understand you...\n")
        say("Please, speak again.")


while(running == True):
    init_speech()