# Izzy: A lightweight, experimental assistant.

# Import core libraries.
import importlib
import os
import sys

# Add a blank function for response-only outputs.
def proceed():
    pass

# Add an array of possible statements.
izzyInputs = [ 
    # User Input     Izzy Output                                   Function   If Manual (true)
    [ "Hello",       "Hello there! Feel free to ask me anything.", proceed(), True ], 
    [ "How are you", "Doing pretty well for a robot.",             proceed(), True ]
]

# Add synonyms for certain words.
izzySynonyms = [
    [ "hello", "hi" ]
]

# Load all of the other scripts.
#if os.path.isdir('/usr/share/izzy/modules'):
#    sys.path.insert(0, '/usr/share/izzy/modules')
#    for i in os.listdir('/usr/share/izzy/modules/'):
#        importlib.import_module(i)
#if os.path.isdir('/home/brent/.config/izzy/modules'):
#    sys.path.insert(0, '/home/brent/.config/izzy/modules')
#    for i in os.listdir('/home/brent/.config/izzy/modules'):
#        importlib.import_module(i)

# Index the synonyms through the existing statements.
for izzyCheck in izzyInputs:
    izzyCheck[0] = izzyCheck[0].casefold()
    if izzyCheck[3]:
        for i in izzySynonyms:
            for j in i:
                if j.casefold() in izzyCheck[0]:
                    for k in i:
                        izzyInputs.append([ izzyCheck[0].replace(j.casefold(), k.casefold()), izzyCheck[1], izzyCheck[2], False ])

# Define the function for interpreting.
def interpret(izzyUserInput):
    # Start a loop for each possible input, check if it is equivalent.
    for izzyCycle in izzyInputs:
        if izzyCycle[0].casefold() == izzyUserInput.casefold():
            # If it is equivalent, give the output, and break.
            return izzyCycle[1]
            break

# Add the help function, and run only it when there are no args.
def izzyHelp():
    print("Izzy: A lightweight, experimental assistant.")
    print("-i, --interpret: Ask a question using a string.")
    print("-h, --help: Shows instructions for the program.")
#if len(sys.argv) == 1:
#    izzyHelp()
#    exit()

# Define a variable for when a parameter needs to be passed
izzyParam = False

# Start interpreting arguments if a parameter is appended or a function.
for i in range(1, len(sys.argv)):
    if izzyParam:
        izzyParam = False
        continue
    if str(sys.argv[i])[0] == "-":
        # Once that is resolved, match the function.
        if sys.argv[i] == "-i" or sys.argv[i] == "--interpret":
            print(interpret(sys.argv[i+1]))
            izzyParam = True
        #elif sys.argv[i] == "-h" or sys.argv[i] == "--help":
            #izzyHelp()
            
