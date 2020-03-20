import mido
from mido.ports import multi_receive
from mido import Message

out_port = "loopMIDI 1" #'Axoloti Core MIDI 1'                  #output port
outCh = 6                         # 6+1  SENDS MIDI TO AXOLOTI ON CHANNEL NR 7

input_ports=["QX49 2"]            # LIST OF CONTROLLERS TO MERGE INTO ONE CH

played_notes = []
print("played_notes : ", played_notes)    #keep track of all notes played TO DO

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
          if (message.control_change.control == 2):
              modWheel = message.control_change.value     # SEND MODWHEEL FROM MICROBRUTE INTO AXOLOTI 
              print(modWheel)
          if (message.control.control != 2):
              port.send(message.control_change-value)     # PASS THROUGH ALL OTHER CC FROM LAUNCHCONTROL XL AND MB
      
except KeyboardInterrupt:
  pass 