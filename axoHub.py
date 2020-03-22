#AxoHub.py
import mido
from mido.ports import multi_receive
from mido import Message

output_ports=mido.get_output_names()
outCh = 6

to_Keyboard = "MicroBrute MIDI 0"
to_Axoloti = 'Axoloti Core MIDI 1'
input_ports=["MicroBrute MIDI 1","Launch Control XL MIDI 1"]
ports = [mido.open_input(name) for name in input_ports]
lineUI = "--------------------------"

localOff = Message('control_change',channel=14,control=122,value=0)

with mido.open_output(to_Keyboard, autoreset=True) as out1:
    out1.send(localOff)
    print("SENDING ",localOff)

print(lineUI)
print(lineUI)
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
                
    with mido.open_output(to_Keyboard, autoreset=True) as kbOut: # open mb output and send midi from axoloti
        for message in multi_receive(ports):
            if hasattr(message,"note"):
                on = Message('note_on',channel=14,velocity=message.velocity,note=message.note)
                kbOut.send(on)
except KeyboardInterrupt:
  pass
