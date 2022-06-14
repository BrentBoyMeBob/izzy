# Izzy: A lightweight, experimental assistant.

# Import main functions.
import izzy.essentials
import sys

# Add the help function, and run only it when there are no args.
def izzyHelp():
    print("Izzy: A lightweight, experimental assistant.")
    print("-i, --interpret: Ask a question using a string.")
    print("-m, --modules: Load Python modules for Izzy in a string, separated by spaces.")
    print("-h, --help: Shows instructions for the program.")
if len(sys.argv) == 1:
    izzyHelp()
    exit()

# Define a variable for when a parameter needs to be passed
izzyParam = False

# Start interpreting arguments if a parameter is appended or a function.
if __name__ == "__main__":
    for i in range(1, len(sys.argv)):
        if izzyParam:
            izzyParam = False
            continue
        if str(sys.argv[i])[0] == "-":
            # Once that is resolved, match the function.
            if sys.argv[i] == "-i" or sys.argv[i] == "--interpret":
                print(izzy.essentials.interpret(sys.argv[i+1]))
                izzyParam = True
            elif sys.argv[i] == "-m" or sys.argv[i] == "--modules":
                izzy.essentials.addModules(sys.argv[i+1])
                izzyParam = True
            elif sys.argv[i] == "-h" or sys.argv[i] == "--help":
                izzyHelp()
