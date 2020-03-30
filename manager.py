import mido,json,argparse,os
from mido import Message
from mido.ports import multi_receive
from os import path

parser = argparse.ArgumentParser(description='''-r or --reset 1 will delete the previous config file
                                                              0 will do nothing    ''')
parser.add_argument('-r','--reset', type=int,default=0)
arguments = parser.parse_args()

outCh = 6
lcontrolCH = 2
midiInputs = mido.get_input_names()
midiOutputs = mido.get_output_names()
inputList = []
inputPort = 0

to_Axoloti = "Axoloti Core MIDI 1"
to_Keyboard = 'MicroBrute MIDI 1'
to_LControl = 'Launch Control XL MIDI 1'

from_axoloti = 'Axoloti Core MIDI 1'
axoPort = mido.open_input(from_axoloti)

style1 = "\x1b[4;37;40m"
greenS = "\x1b[6;30;42m"
redS = "\x1b[1;36;41m"
greenLetters = "\x1b[1;33;40m"

def loggit(text,style):
                return print(style + text + " \x1b[0m ")

if arguments.reset == 1 :
        if path.exists("stored_midiIO.json"):
                loggit("RESETTING!!",greenS)
                os.remove("stored_midiIO.json")
        else:
                loggit('Config file is not in the folder or has been removed',redS)

def choose(text):
        return int(input(text))

def startMenu():

        loggit("----------- . -----------",greenS)
        print("\x1b[6;30;42m STARTING I/0 SETTUP \x1b[0m      ----------- \x1b[1;33;40m < this settings will be stored in stored_midiIO.json > \x1b[0m")
        loggit("----------- . -----------",greenS)
        loggit("----------- . -----------",greenS)
        loggit("----------- INPUTS -----------",greenS)

        for name in mido.get_input_names():
                loggit("Input : "+ name,greenLetters)

        loggit("\n ----------- OUTPUTS -----------",greenS)
        for name in mido.get_output_names():
                        loggit("Output : " +name,greenLetters)

        print("----------- . ----------- \n")

        for input in midiInputs:
                inIndex = midiInputs.index(input)
                print(midiInputs[inIndex])
                addOrNot = choose("Add "+str(midiInputs[inIndex]) +" To inputs ? (1.- Yes  2.- No :  ")
                if addOrNot == 1:
                        inputList.append(midiInputs[inIndex])
                elif addOrNot != 1:
                        pass
                else:
                        pass
        print("ADDED CHANNELS TO MERGE")
        print("-------------- . ------------- \n")

        for name in midiOutputs:
                print(name, midiOutputs.index(name), "\x1b[1;36;41m <--SELECT  \x1b[0m ")

        outnumPort = choose(" \n []Choose an output port[] :  ")
        to_Axoloti = midiOutputs[outnumPort]


        print("INPUT ",midiInputs," OUTPUT ",midiOutputs[outnumPort])
        loggit('\n ----- \n READY \n ROUTIG STARTING... \n -----\n',greenLetters)

        #store new data in json file
        config = {'input': midiInputs, 'output': to_Axoloti}
        with open('stored_midiIO.json', 'w') as f:
                json.dump(config, f)

        loggit('\n ----- PREFERECES SAVED IN .\stored_midiIO.json -----\n',greenLetters)

if path.exists("stored_midiIO.json"):                                           #load data from the previously choosen settings
        with open('stored_midiIO.json', 'r') as f:
                        config = json.load(f)
                        inputPort = config["input"]
                        inputList = inputPort
                        to_Axoloti = config["output"]
                        print("\x1b[6;30;42m LAST USED CONFIGURATION LOADED  \x1b[0m \n")
                        print("INPUT ",inputPort," OUTPUT  ",to_Axoloti)
                        print("\x1b[4;37;40m Success! \x1b[0m")
        pass

else:
        startMenu()
        pass

ports = [mido.open_input(name) for name in inputList]

############# send custom CC local off for keyboard
local_off = Message('control_change',channel=13,control=122,value=0)

with mido.open_output(to_Keyboard, autoreset=True) as kb:
  kb.send(local_off)
####################################

try:
  with mido.open_output(str(to_Axoloti), autoreset=True) as port:
    for message in multi_receive(ports):
      if hasattr(message, "note"):
        print(message)
        if message.type == 'note_on':
          on = Message('note_on',channel=outCh,velocity=message.velocity,note=message.note)
          port.send(on)

        if message.type == 'note_off':
          off = Message('note_off',channel=outCh,note=message.note)
          port.send(off)

      if message.type == 'control_change' :
        cc = Message('control_change',channel=outCh,control=message.control,value=message.value)
        port.send(cc)
        print("Sending : ", cc)
        print("----------------------")

# To receive led CC data to show in the Launch Control XL
  with mido.open_output(to_LControl) as port2:
    print("Opened out to lx and axo listener " ,to_LControl, port2)
    for message in multi_receive(axoPort):
      if message.type == 'control_change' :
        ledCC = Message('control_change',channel=lcontrolCH,control=message.control,value=message.value)
        port2.send(ledCC)
        print("Sending LED CC VALUES FROM AXO TO LXL")

except KeyboardInterrupt:
  pass