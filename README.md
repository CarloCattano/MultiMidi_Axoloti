# Raspberry Pi as a USB Midi Hub for<a href="https://github.com/axoloti/axoloti/releases/tag/2.0.0/"> Axoloti 2.0 </a>

### this script uses <a href="https://pypi.org/project/mido/">mido</a> library to create a simple example of passing midi to the raspberry pi . inspired by @logsol idea
### of merging several midi channels into one to overcome Axoloti usb hub limitations 

#### I will slowly develope an untility and make it usable in any setup as long as my free time allows me 
 
#### - You will rtmidi :
           pip3 install python-rtmidi mido
##### And depending on your raspberry pi operating system some aditional libraries and jack1 too probably . ( will confirm all dependencies once the general script is polished)

         python multiMidi.py
##### to use it with your own gear for now you can substitute the input_ports names with your own controllers connected to the
##### raspberry pi via USB. 
