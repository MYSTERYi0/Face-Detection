# Face-Recognition ###
## Basic Concepts and implementation of Face recognition using OpenCV in python 3.

The images taken in the input needs to be converted into B/W image since this will help haarcascade recognize the images perfectly.

### >For images
    You can see your face recognised by the web camera off the Laptop or computer.

   `haarcascade_frontalface_default.xml` is the .xml file that is going to help us for recognising the faces.

   Rest is the logic that will be help us in the py code. 
   The loops in the image is used to recognise various faces at once.

  * Accepting Image input.
  * Converting it to B/W image.
  * Using `haarcascade_frontalface_default.xml` to recognize the face(s).
  * Performing operations using OpenCV.
  * Forming a rectangle aroung the face.

### >For Videos

   What is Video?

  --> Video is collection of images! The images when put together seems like a video.

  Using this logic we will allow the code to access the webcam and continuoulsy recognise the face in the image.
  The same logic of the program will be used for video:

  * Accepting Image input.
  * Converting it to B/W image.
  * Using `haarcascade_frontalface_default.xml` to recognize the face(s).
  * Performing operations using OpenCV.
  * Forming a rectangle aroung the face.
  * Implementing a loop to apply the effects in each frame of the video.
