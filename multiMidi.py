import mido
from mido.ports import multi_receive
from mido import Message

out_port = 'Axoloti Core MIDI 1'
outCh = 6

input_ports=["MicroBrute MIDI 1","Launch Control XL MIDI 1"]

print("inputs " ,mido.get_input_names())
print("----------------------------------- \n ")
print(mido.get_output_names())
print("----------------------------------- \n ")


ports = [mido.open_input(name) for name in input_ports]
print("ports ",ports)
for port in ports:
  print('Using {}'.format(port))
print('Waiting for messages...')

try:
  with mido.open_output(out_port, autoreset=True) as port:
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

except KeyboardInterrupt:
  pass