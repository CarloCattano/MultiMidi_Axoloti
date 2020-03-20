import mido
from mido.ports import multi_receive
from mido import Message

out_port = 'loopMIDI 1'                       
outCh = 6                         

input_ports=["Launch Control XL 2"]         

played_notes = []
print("played_notes : ", played_notes)   

print("inputs " ,mido.get_input_names())
print(mido.get_output_names())


ports = [mido.open_input(name) for name in input_ports] 
print("ports ",ports)
for port in ports:
  print('Using {}'.format(port))
print('Waiting for messages...')

try:
  with mido.open_output(out_port, autoreset=True) as port:
    for message in multi_receive(ports):
                                                        # SEE ALL RECEIVED MESSAGES 
      if hasattr(message, "note"):
        currNote = message                               #HOLD THE CURRENT NOTE AND PASS IT THROUGH TO THE AXOLOTI ON CH 7
        if message.type == 'note_on':
          on = Message('note_on',channel=outCh,velocity=currNote.velocity,note=currNote.note)
          port.send(on)
        if message.type == 'note_off':
          off = Message('note_off',channel=outCh,note=currNote.note)
          port.send(off)
      if message.type == 'control_change' :
        cc = Message('control_change',channel=outCh,control=message.control)
        port.send(message)
        # print("Sending : ", message)
        # print("Sending : ", cc)
        # print("----------------------")
       
except KeyboardInterrupt:
  pass 