import sys
import mido
from mido.ports import multi_receive
from mido import Message
                      
print("\n MIDI INPUTS : " ,mido.get_input_names())
print("\n MIDI OUTPUTS : ",mido.get_output_names())

if len(sys.argv) < 4:
    print("\n ------- \n PLEASE PROVIDE  [input_port out_port outCh] (1-16) 3 ARGUMENTS \n ---------\n")
elif len(sys.argv) > 3 :
    print("\n starting..............\n","-------------------")
    input_ports = sys.argv[1]
    out_port = sys.argv[2]                      
    outCh = sys.argv[3]

    print("input_ports",input_ports)
    print("out_port",out_port)
    print("outCh",outCh)

