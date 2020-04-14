import speech_recognition as sr
import os

r = sr.Recognizer()

def getVoice(file):
  # turning the audio file into text 
  # this is using test.wav
  with sr.AudioFile(file) as source:
    print('Speak Anything')

    # listening for audio
    audio = r.listen(source)

    try: 
      # turning audio into text
      text = r.recognize_google(audio)
    except:
      # in case of error, don't say anything!
      text = ""

  print(text)

    # removing test.wav to save space
  os.remove(file)

  return text