import speech_recognition as s_r
import pyttsx3

import gtts
from playsound import playsound


print(s_r.__version__)
r = s_r.Recognizer()
engine = pyttsx3.init()

my_mic = s_r.Microphone(device_index=1)
with my_mic as source:
    print("Say now!!!!")
    audio = r.listen(source)
    engine.save_to_file(audio , "saya.mp3")
    
   

    #take voice input from the microphone
print(r.recognize_google(audio))
t = str(r.recognize_google(audio))

engine.runAndWait()

tts = gtts.gTTS(t)
tts.save("saya.mp3")
playsound("saya.mp3")


engine.stop()



