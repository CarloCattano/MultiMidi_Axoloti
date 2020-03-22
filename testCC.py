import sys
import mido
from mido.ports import multi_receive
from mido import Message

def StartMenu():
    input_ports=mido.get_input_names()
    output_ports=mido.get_output_names()

    lineUI = "--------------------------"

    for item in input_ports:
        print("input_ports ",item ," Select " ,input_ports.index(item)+1,lineUI)
    chooseIn = int(input("Choose an input  : ")) -1
    print(lineUI)

    for item in output_ports:
        print("output_portst ",item," Select " ,output_ports.index(item)+1,lineUI)
    chooseOut = int(input("Choose an ouput  : ")) -1
    print(lineUI)


    _inport = mido.open_input(input_ports[chooseIn])
    print("Input port choosen : ", _inport)
    print(lineUI)

    localOff = Message('control_change',channel=14,control=122,value=0)
    with mido.open_output(output_ports[chooseOut], autoreset=True) as out1:
        out1.send(localOff)
        print("SENDING ",localOff)

    print(lineUI)
    #return [input_ports[chooseIn],output_ports[chooseOut]]  # return the result of the function ? to main script 

# if len(sys.argv) < 4:
#     print("\n ------- \n PLEASE PROVIDE  [input_port out_port outCh] (1-16) 3 ARGUMENTS \n ---------\n")
# elif len(sys.argv) > 3 :
#     print("\n starting..............\n","-------------------")
#     input_ports = sys.argv[1]
#     out_port = sys.argv[2]                      
#     outCh = sys.argv[3]

#     print("input_ports",input_ports)
#     print("out_port",out_port)
#     print("outCh",outCh)

