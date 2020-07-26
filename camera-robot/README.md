# LTE Camera Robot Controller

This app enables a robot car to carry a cell phone around in order to utilize the phone's camera and cellular capabilities. In theory, the operator should be able to drive the car anywhere that the phone has a cellular connection. 

The idea that I can sit in my house and drive my little car to basically anywhere in the world is super cool to me. I've seen videos of RC drones, planes, and even boats with this functionality and it amazes me every time.

This project has three components:
* Server code that displays the camera from the phone on the robot, and that sends back driving commands to the phone
* A phone app that uses a web communication protocol to livestream the camera to the computer and receive the commands which are then sent to the Arduino connected via USB
* Code running on the Arduino that receives commands from the phone and drives the robot's motors accordingly

### Server code
A Python web server with Flask communicates with a matplotlib plot that displays the image and responds to keypress events. Whenever the phone makes a POST request to the server with the latest camera image, the server responds with a speed for the left and right motor determined by the user input.

The biggest challenge I had with this project was how I exposed my local network ports to the internet. At first, I was using [ngrok](https://ngrok.com/). The free tier of ngrok allows only a small number of unique connections, and for some reason each request the phone made created a new connection instead of keeping alive an existing connection. This only happened when my phone was on its cellular connection and not when it was on a wifi connection. I tried setting various HTTP headers on both server and client sides, but I never succeeded in solving this issue.

To get around this, I ended up used [Pagekite](https://pagekite.net/) because their free tier either doesn't terminate my connections, or because it doesn't have a unique connection limit. This is a hacky solution but it works.

### Phone app
I used Flutter for the Android app because it streamlines the process of obtaining a live camera preview feed. Then, I used Flutter's platform channels so I could write Java code to process the images. 

Running Java code through platform channel is also crucial to the serial communication with the Arduino. I used [this USB library](https://github.com/felHR85/UsbSerial) to handle the serial communication once I established the USB connection. I expected the serial communication to be difficult, but it was actually wasn't too bad. 

### Arduino code
The code on the Arduino is simple: it reads 8 characters of serial data which is split into two integers, and it then sets the respective motor's speed to those integer values. 

### Car chassis
The first version of the chassis used all parts from a simple car kit. I found that this chassis was too small to hold the phone, the 3D printed phone mount, the USB hub, the long USB cable, the battery pack, and the Arduino. Also, the wheels were too small to be used outdoors. For the second version of the chassis, I designed and 3D printed new larger wheels and cut a sheet of acrylic that was large enough to fit all the components. The second version of the chassis worked very well outside.

### Extensions
* Use the server code to set location waypoints that the car drives navigates to, similar to commercial long-range robot software
* Implement a different communication method that allows for faster and more frequent communication (like websockets)
* Use a real web server instead of Flask
* Use a real hosting service instead of ngrok or Pagekite
