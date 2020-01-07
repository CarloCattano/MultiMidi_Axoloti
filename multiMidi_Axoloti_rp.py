import mido
from mido.ports import multi_receive
from mido import Message

out_port = 'Axoloti Core MIDI 1'  

input_ports=["MicroBrute MIDI 1","Launch Control XL MIDI 1"] # LIST OF CONTROLLERS TO MERGE INTO ONE CH

ports = [mido.open_input(name) for name in input_ports] 

for port in ports:
  print('Using {}'.format(port))
print('Waiting for messages...')

try:
  with mido.open_output(out_port, autoreset=True) as port:
    for message in multi_receive(ports):
      print(message)                            # SEE ALL RECEIVED MESSAGES 
      if hasattr(message, "note"):
       currNote = message.note      #HOLD THE CURRENT NOTE AND PASS IT THROUGH TO THE AXOLOTI ON CH 7
       if message.type == 'note_on':
        on = Message('note_on',channel=6,velocity=127,note=currNote)
        port.send(on)

       if message.type == 'note_off':
        off = Message('note_off',channel=6,note=currNote)
        port.send(off)

       if hasattr(message, "control_change"):
        if (message.control_change.control == 2):
            modWheel = message.control_change.value     # SEND MODWHEEL FROM MICROBRUTE INTO AXOLOTI 
            print(modWheel)
        if (message.control.control != 2):
            port.send(message.control_change-value)     # PASS THROUGH ALL OTHER CC FROM LAUNCHCONTROL XL AND MB

except KeyboardInterrupt:
    pass