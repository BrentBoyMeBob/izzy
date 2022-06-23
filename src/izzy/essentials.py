# Import core functions.
import importlib
import os
import sys

# Add a blank function for response-only outputs.
def proceed():
    pass

# Add an array of possible statements.
izzyInputs = [ 
    # User Input            Izzy Output         Function    To Fix (true)
    [ "hello",              "Hey there!",       proceed,    True ],
    [ "how are you doing",  "I'm doing well.",  proceed,    True ]
]

# Add synonyms for certain words.
izzySynonyms = [
    [ "hello", "hi", "hey" ]
]

# Index the synonyms through the existing statements. Create a function for external use.
def indexPossibilities():
    izzyForDeletion = []
    for izzyCheckGarbage in range(len(izzyInputs)):
        izzyCheckGarbageParam = izzyInputs[izzyCheckGarbage]
        if izzyCheckGarbageParam[3] is False:
            izzyForDeletion.append(izzyCheckGarbage)
    for izzyDeleteProcess in reversed(izzyForDeletion):
        izzyInputs.pop(izzyDeleteProcess)
    for izzyCheck in izzyInputs:
        izzyCheck[0] = izzyCheck[0].casefold()
        if izzyCheck[3]:
            for i in izzySynonyms:
                for j in i:
                    if j.casefold() in izzyCheck[0]:
                        for k in i:
                            izzyInputs.append([ izzyCheck[0].replace(j.casefold(), k.casefold()), izzyCheck[1], izzyCheck[2], False ])
indexPossibilities()

# Create a function to add Python modules for Izzy to reference and index.
def addModules(izzyModules):
    izzyModuleList = izzyModules.split(" ")
    for izzyModuleToImport in izzyModuleList:
        importlib.import_module(izzyModuleToImport)
    indexPossibilities()

# Create a fallback statement if there were no correct interpretations.
def fallbackEvent():
    return "I couldn't understand."
fallbackCall = fallbackEvent

# Define the function for interpreting.
def interpret(izzyUserInput):
    interpret.izzyUnformedInput = izzyUserInput
    # Create a formed input.
    interpret.izzyFormedInput = [ interpret.izzyUnformedInput ]
    for i in range(len(interpret.izzyFormedInput)):
        interpret.izzyFormedInput[i] = interpret.izzyFormedInput[i].casefold()
        izzyForm = True
        while(izzyForm):
            def breakdown(toReplace):
                interpret.izzyBackupInput = interpret.izzyFormedInput[i]
                interpret.izzyFormedInput.pop(i)
                interpret.izzyFormedInput += interpret.izzyBackupInput.split(toReplace)
            if ", and " in interpret.izzyFormedInput[i]:
                breakdown(", and ")
            if ", " in interpret.izzyFormedInput[i]:
                breakdown(", ")
            if " and " in interpret.izzyFormedInput[i]:
                breakdown(" and ")
            if "." in interpret.izzyFormedInput[i]:
                breakdown(".")
            if "?" in interpret.izzyFormedInput[i]:
                breakdown("?")
            if "!" in interpret.izzyFormedInput[i]:
                breakdown("!")
            izzyForm = False
    # Start a loop for each possible input, check if it is equivalent.
    izzyResults = []
    for i in interpret.izzyFormedInput:
        izzyFound = False
        for izzyCycle in izzyInputs:
            if izzyCycle[0].casefold() == i:
                # If it is equivalent, give the output, and break.
                izzyFound = True
                izzyResults.append(izzyCycle[1])
                izzyCycle[2]()
                break
        # If none of them are equivalent, execute the modular Fallback Call.
        if izzyFound is False: 
            izzyResults.append(fallbackCall())
    # Now, merge all of the answers into one string and return it to complete the function.
    izzyFinalResult = ""
    if len(izzyResults) > 1:
        for i in range(len(izzyResults)):
            if i != 0:
                if izzyResults[i][0] is not "I":
                    izzyResults[i] = izzyResults[i][0].casefold() + izzyResults[i][1:]
            if i == len(izzyResults)-1:
                pass
            elif i == len(izzyResults)-2:
                izzyResults[i] = izzyResults[i].replace(".", " and ")
                izzyResults[i] = izzyResults[i].replace("?", " and ")
                izzyResults[i] = izzyResults[i].replace("!", " and ")
            else:
                izzyResults[i] = izzyResults[i].replace(".", ", ")
                izzyResults[i] = izzyResults[i].replace("?", ", ")
                izzyResults[i] = izzyResults[i].replace("!", ", ")
            izzyFinalResult += izzyResults[i]
    else:
        izzyFinalResult += izzyResults[0]
    return izzyFinalResult
