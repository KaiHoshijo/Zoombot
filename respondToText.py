import pyttsx3
import os

engine = pyttsx3.init()

def response(text):
  # ensuring lower case text from the audio file
  text = text.lower()
  # the new file
  changed = ""
  # when changing the image file to default, this ensures it can be changed back
  test = "Images/test.jpg"
  test1 = "Images/test1.jpg"
  default = "Images/Default.jpg"

  # a bunch of if-elif-else cases for responses
  if "how are you" in text: 
    changed = "Images/thinking.jpg"
    output = "I am good. How are you?"
  elif "how is school" in text or "how's school" in text: 
    changed = "Images/talking.jpg"
    output = "It's going well. I have all A's!"
  elif "god" in text:
    changed = "Images/interested.jpg"
    output = "Breaking the first commandment"
  elif "earth" in text:
    changed = "Images/interested.jpg"
    output = "The earth is flat and you can't change my mind"
  elif "meeting" in text:
    changed = "Images/talking.jpg"
    output = "Can we circle back to that"
  elif "isolation" in text:
    changed = "Images/talking.jpg"
    output = "Isolation is going well. I have programmed a lot"
  elif "sorry, messed up video" == text:
    changed = "Images/talking.jpg"
    output = "Sorry, my video is glitchy."
  elif "kai" in text:
    changed = "Images/thinking.jpg"
    output = "That is my name. Don't wear it out"
  else: output = ""

  # saying the output to the peoples listening
  engine.say(output)
  engine.setProperty('rate', 120)
  engine.setProperty('volume', .9)
  # ensuring that the files get changed back accordingly
  try: 
    os.rename(default, test)
    os.rename(changed, default)
    engine.runAndWait()
    os.rename(default, test1)
    os.rename(test, default)
    os.rename(test1, changed)
  except:
    os.rename(test, default)