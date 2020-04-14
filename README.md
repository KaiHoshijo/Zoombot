# Zoombot
This was based off of Matt Reed on his blog:
https://redpepper.land/blog/zoombot/ 

## Requirements that I found to ensure that this works: <br/>
  You will need to enable **Stero Mix on Windows** <br/>
    For Linux and Mac distros, you would need to install another virtual mic and use that for the program <br/>
  You will need to download **OBS camera and its virtual camera** <br/>
    Ensure that you have an image created and pointed to *Default.jpg*
  
### While running the zoom call, you need **OBS** open to be able to access the virtual camera <br/>
  Don't forget to share audio with everyone on the zoom call so that they can hear the responses <br/>
  
## How it works:
  It uses a combination of a few python scripts to take audio from those speaking on the call and puts it into a video file "test.wav" <br/>
  It then processes "test.wav" and converts it to text and passes it onto the chatbot portion <br/>
  In the chatbot portion, it checks for text similarities to respond to and will change the picture based off that <br/>
    That works by changing picture names to Default.jpg since OBS is pointed to that filename <br/>
  After changing the picture, it turns that text to speech and reads it to those listening <br/>
