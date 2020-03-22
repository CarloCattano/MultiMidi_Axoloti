#AxoHub.py
import mido
from mido.ports import multi_receive
from mido import Message

#to_Axoloti = 'Axoloti Core MIDI 1'
#to_Keyboard = 'MicroBrute MIDI 0'

# outCh = 6

# input_ports=["MicroBrute MIDI 1","Launch Control XL MIDI 1"]

# print("inputs " ,mido.get_input_names())
# print("----------------------------------- \n ")
# print(mido.get_output_names())
# print("----------------------------------- \n ")

# ports = [mido.open_input(name) for name in input_ports]

# print("\n input ports ",ports)

# for port in ports:
#   print('Using {}'.format(port))

# print('\n ----- \n Waiting for messages...\n -----\n')

input_ports=mido.get_input_names()
output_ports=mido.get_output_names()  

lineUI = "--------------------------"

for item in input_ports:
    print("input_ports ",item ," Select " ,input_ports.index(item)+1,lineUI)
chooseIn = int(input("Choose an input  : ")) -1
to_Axoloti = str(input_ports[chooseIn])
print("TO AXOLOTI !!!!!!!  ",to_Axoloti)
print(lineUI)

for item in output_ports:
    print("output_portst ",item," Select " ,output_ports.index(item)+1,lineUI)
chooseOut = int(input("Choose an ouput  : ")) -1
to_Keyboard = output_ports[chooseOut]
print(lineUI)

to_Axoloti = mido.open_input(input_ports[chooseIn])
print("Input port choosen : ", to_Axoloti)
print(lineUI)

localOff = Message('control_change',channel=14,control=122,value=0)

with mido.open_output(to_Keyboard, autoreset=True) as out1:
    out1.send(localOff)
    print("SENDING ",localOff)

print(lineUI)

try:
  with mido.open_output(to_Axoloti, autoreset=True) as port:
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
 with mido.open_output(to_Keyboard, autoreset=True) as kbOut:
     for message in multi_receive(ports):
        if hasattr(message,"note"):
            on = Message('note_on',channel=14,velocity=message.velocity,note=message.note)
            kbOut.send(on)
except KeyboardInterrupt:
  pass
