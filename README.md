# Zoombot
This was based off of Matt Reed on his blog:
https://redpepper.land/blog/zoombot/ 

Requirements that I found to ensure that this works:
  You will need to enable Stero Mix on Windows.
    For Linux and Mac distros, you would need to install another virtual mic and use that for the program
  You will need to download OBS camera and its virtual camera
    Ensure that you have an image created and pointed to Default.jpg
  
While running the zoom call, you need OBS open to be able to access the virtual camera
  Don't forget to share audio with everyone on the zoom call so that they can hear the responses
  
How it works:
  It uses a combination of a few python scripts to take audio from those speaking on the call and puts it into a video file "test.wav"
  It then processes "test.wav" and converts it to text and passes it onto the chatbot portion
  In the chatbot portion, it checks for text similarities to respond to and will change the picture based off that
    That works by changing picture names to Default.jpg since OBS is pointed to that filename
  After changing the picture, it turns that text to speech and reads it to those listening
