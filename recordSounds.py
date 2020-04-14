import pyaudio, wave, sys

def saveAudio(filename):
  # all the basic information to get audio file
  CHUNK = 1024
  FORMAT = pyaudio.paInt16
  CHANNELS = 1
  RATE = 44100

  # getting the audio from the speaker
  p = pyaudio.PyAudio()
  for i in range(0, p.get_device_count()):
    if "Stero Mix" in p.get_device_info_by_index(i)['name']: device_index = i
    else: device_index = 1

  # opening the stream to start listening
  stream = p.open(format = FORMAT,
                  rate = RATE,
                  input = True,
                  channels = CHANNELS,
                  frames_per_buffer=CHUNK,
                  input_device_index=device_index)

  all = []
  print("recording!!!")
  beginning = True
  # run while there is talking or there is silence
  while True:

    # read in data from the stream of stero mix
    data = stream.read(CHUNK)
    all.append(data)
    # print("data", data[0], data[1], data[2], data[3])
    
    sample = [data[0], data[1], data[2], data[3]]
    # check if there is talking or silence
    if beginning == True and (255 in sample or 254 in sample or 1 in sample or [0, 0, 0, 0] == sample): 
      # print("continue", sample)
      continue
    elif True in [True for point in sample if point > 1 and point < 254]: 
      # print("sound detected", sample)
      beginning = False
    elif beginning == False and (255 in sample or 254 in sample or 1 in sample or [0, 0, 0, 0] == sample): 
      # print("end", sample)
      break

  # no more talking so the file is done!
  stream.stop_stream()
  stream.close()
  p.terminate()
  print("finished!!!")

  # saving the file as a wav to pass onto getVoice
  data = b''.join(all)
  wf = wave.open(filename, 'wb')
  wf.setnchannels(CHANNELS)
  wf.setsampwidth(p.get_sample_size(FORMAT))
  wf.setframerate(RATE)
  wf.writeframes(data)
  wf.close()