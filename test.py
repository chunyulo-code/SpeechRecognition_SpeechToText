import speech_recognition
import time
import datetime
import win32gui, win32ui, win32con, win32api

print("Hello World!!!")
r = speech_recognition.Recognizer()

with  speech_recognition.Microphone() as source:
    print('Speak Anything: ')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='en-US')
        print('You said : {}'.format(text))
    except:
        print('Sorry, could not recognize your voice')

f=open(r"D:\SpeechRecognition\result.txt","w")
f.write(text)
f.close()
print(text)
