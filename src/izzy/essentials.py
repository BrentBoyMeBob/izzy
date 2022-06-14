# Import core functions.
import importlib
import os
import sys

# Add a blank function for response-only outputs.
def proceed():
    pass

# Add an array of possible statements.
izzyInputs = [ 
    # User Input          Izzy Output                                   Function     To Fix (true)
    [ "Hello",            "Hello there! Feel free to ask me anything.", "proceed()", True ], 
    [ "How are you",      "Doing pretty well myself.",                  "proceed()", True ]
]

# Add synonyms for certain words.
izzySynonyms = [
    [ "hello", "hi", "hey" ]
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
#    import bender

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
            exec(izzyCycle[2])
            break
