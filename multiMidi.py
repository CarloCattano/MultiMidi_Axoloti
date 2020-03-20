import mido
from mido.ports import multi_receive
from mido import Message

out_port = "Axoloti Core MIDI 1"                       
outCh = 6                         

input_ports=["MicroBrute MIDI 1","Launch Control XL MIDI 1"]         

played_notes = []
print("played_notes : ", played_notes)   

print(mido.get_input_names())
print(mido.get_output_names())


ports = [mido.open_input(name) for name in input_ports] 
print("ports ",ports)
for port in ports:
  print('Using {}'.format(port))
print('Waiting for messages...')


try:
  with mido.open_output(out_port, autoreset=True) as port:
    for message in multi_receive(ports):
      print(message)                                     # SEE ALL RECEIVED MESSAGES 
      if hasattr(message, "note"):
        currNote = message                               #HOLD THE CURRENT NOTE AND PASS IT THROUGH TO THE AXOLOTI ON CH 7
        if message.type == 'note_on':
          on = Message('note_on',channel=outCh,velocity=currNote.velocity,note=currNote.note)
          port.send(on)
        if message.type == 'note_off':
          off = Message('note_off',channel=outCh,note=currNote.note)
          port.send(off)
        if hasattr(message, "control_change"):
              # SEND MODWHEEL FROM MICROBRUTE INTO AXOLOTI 
              port.send(message.control_change)     # PASS THROUGH ALL OTHER CC FROM LAUNCHCONTROL XL AND MB
              print("Sending CC : ", message.control_change)
except KeyboardInterrupt:
  pass 