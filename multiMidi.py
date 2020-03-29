import time
import mido
from mido.ports import multi_receive
from mido import Message

to_Axoloti = 'Axoloti Core MIDI 1'
to_Keyboard = 'MicroBrute MIDI 1'

outCh = 6 # This is the note channel I want to send to the axoloti +1 so its channel 7 

input_ports=["MicroBrute MIDI 1","Launch Control XL MIDI 1"] # add your controller name as its shown on the console

print("inputs " ,mido.get_input_names())
print("----------------------------------- \n ")
print(mido.get_output_names())
print("----------------------------------- \n ")

ports = [mido.open_input(name) for name in input_ports]

print("\n input ports ",ports)

for port in ports:
  print('Using {}'.format(port))

print('\n ----- \n Waiting for messages...\n -----\n')

local_off = Message('control_change',channel=13,control=122,value=0)
with mido.open_output(to_Keyboard, autoreset=True) as kb:
  time.sleep(1)
  kb.send(local_off)

try:
  with mido.open_output(to_Axoloti, autoreset=True) as port:
<<<<<<< HEAD
    for message in multi_receive(ports):
        if hasattr(message, "note"):
          currNote = message
          if message.type == 'note_on':
              on = Message('note_on',channel=outCh,velocity=currNote.velocity,note=currNote.note)
              port.send(on)
              #print(on)
          if message.type == 'note_off':
              off = Message('note_off',channel=outCh,note=currNote.note)
              port.send(off)
        if message.type == 'control_change' :
          cc = Message('control_change',channel=outCh,control=message.control,value=message.value)
          port.send(cc)
          #print("Sending : ", cc)
          #print("----------------------")
=======
    for message in multi_receive(ports):                                     
      if hasattr(message, "note"):
        currNote = message                               
        if message.type == 'note_on':
          on = Message('note_on',channel=outCh,velocity=currNote.velocity,note=currNote.note)
          port.send(on)

        if message.type == 'note_off':
          off = Message('note_off',channel=outCh,note=currNote.note)
          port.send(off)
          
      if message.type == 'control_change' :     
        cc = Message('control_change',channel=outCh,control=message.control,value=message.value)
        port.send(cc)
        print("Sending : ", cc)
        print("----------------------")

>>>>>>> 5b337c53be466cb34b8e40265498c4533d06cfda
except KeyboardInterrupt:
  pass
