import mido,json,argparse,os
from mido import Message
from mido.ports import multi_receive
from os import path
from tkinter import *

window = Tk()
window.geometry("350x200")
window.title("welcome to tkinter ")

parser = argparse.ArgumentParser(description='Configure the script')
parser.add_argument('--reset', type=int,default=False)
arguments = parser.parse_args()

outCh = 6 # 
midiInputs = mido.get_input_names()
midiOutputs = mido.get_output_names()
inputList = []
midiin = "loopMIDI 1 0"
outputPort = 0
inputPort = 0

port = mido.open_input("loopMIDI 1 0")

def updateLabel(x):
	if  x in midiInputs:
		midiInputs.remove(midiInputs[x])
	if x not in midiInputs:
		midiInputs.append(midiInputs[x])
	textvar = " INPUT "  + midiInputs[x]
	lab1 = Label(window, text=textvar, relief=RAISED,height=8, width=50 )
	print ("NAME APPENDED ",midiInputs[x])
	
	lab1.pack()

for i in range(len(midiInputs)):
		button = Button() 
		button.configure(text=midiInputs[i])#This works fine for assigning text to the buttons. Each date value is unique for each button.
		button['command'] = lambda: updateLabel(i)
		button.pack(side=LEFT)
		

if arguments.reset == 1 :
	if path.exists("stored_midiIO.json"):
		print("\x1b[1;36;41m RESETTING!! \x1b[0m")
		os.remove("stored_midiIO.json")
	else:
		print('\x1b[1;36;41m Config file is not in the folder or has been removed \n \x1b[0m')

def startMenu():
	print("----------- . -----------")
	print("\x1b[6;30;42m STARTING I/0 SETTUP \x1b[0m      ----------- \x1b[1;33;40m < this settings will be stored in stored_midiIO.json > \x1b[0m")
	print("----------- . -----------\n")
	print("----------- INPUTS -----------") 

	for name in mido.get_input_names():
			print("Input : ", name)

	print("\n ----------- OUTPUTS -----------")
	for name in mido.get_output_names():
			print("Output : " , name)
	print("----------- . ----------- \n")

	

	for name in midiInputs:
		print("[",name,  "] Select nº " ,midiInputs.index(name))
		
	numPort = int(input("Choose an input port : "))
	inputPort = midiInputs[numPort]

	for name2 in midiOutputs:
		print("[",name2,midiOutputs.index(name2), "] Select nº ", midiOutputs.index(name2))
	
	print("-------------- . ------------- \n")

	outnumPort = int(input("Choose an output port : "))

	print("INPUT ",midiInputs[numPort]," OUTPUT ",midiOutputs[outnumPort])
	print('\n ----- \n READY \n ROUTIG STARTING... \n -----\n')
	config = {'input': midiInputs[numPort], 'output': midiOutputs[outnumPort]}


	
	with open('stored_midiIO.json', 'w') as f:
		json.dump(config, f)

if path.exists("stored_midiIO.json"):   					#load data from the previously choosen settings
	with open('stored_midiIO.json', 'r') as f:
			config = json.load(f)
			inputPort = config["input"]
			outputPort = config["output"]
			print("\x1b[6;30;42m LAST USED CONFIGURATION LOADED \n \x1b[0m")
			print("INPUT ",inputPort," OUTPUT  ",outputPort)
			print("\x1b[4;37;40m Success! \x1b[0m")

		
else:
	startMenu()	   

try:
	window.mainloop()
except KeyboardInterrupt:
	pass