import fileinput

for line in fileinput.input(): #if no args to input(), read from stdin
    pass

#--------------
import sys

for line in sys.stdin: #stdin can be used like a file object
    print line
#or
input_text = "".join(sys.stdin)

#--------------
inputText = input("message") #prompts input

#--------------
file = open("file.txt", "r")
file.readline()
file.read() #whole file