import getVoice, recordSounds, respondToText

if __name__ == "__main__":
  # have the program start off with a joke
  respondToText.response("Sorry, messed up video")
  # run this program until the call is over
  while True:

    # save input from speaker output
    recordSounds.saveAudio("test.wav")

    # get the text from the audio file
    text = getVoice.getVoice("test.wav")

    # respond to the text in test.wav
    respondToText.response(text)