# Use your raspberry pi as a usb Midi Hub to use several controllers with your axoloti

### this script uses mido<url>https://pypi.org/project/mido/</url> library to create a simple example of passing midi to the raspberry pi . inspired by @logsol idea
### of merging several midi channels into one to overcome Axoloti usb hub limitations 

#### I will slowly develope an untility and make it usable in any setup as long as my free time allows me 
 
#### - You will rtmidi :
           pip3 install python-rtmidi
##### And depending on your raspberry pi operating system some aditional libraries and jack1 too probably . ( will confirm all dependencies once the general script is polished)

         python multiMidi.py
##### to use it with your own gear for now you can substitute the input_ports names with your own controllers connected to the
##### raspberry pi via USB. 
