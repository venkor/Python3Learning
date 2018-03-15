# It import the argv modules from sys library
from sys import argv
# Unpacks the arguments into variables from left to right
script, input_file = argv
# defines a function print_all that takes one argument and reads it
def print_all(f):
    print(f.read())
# defines a function rewind that sets the offset position to 0 of the read/write pointer within the file.
def rewind(f):
    f.seek(0)
# defiens a function print_a_line that takes two arguments, the line_count and f - it prints the line from f.
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")
# sets a variable is assigned to open the input_file given in script run
current_file = open(input_file)

print("First let's print the whole file:\n")
# calls the prin_all function which reads the current_file and prints it to terminal
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# runs the rewind function, which sets the offset position back to 0 for the current_file
rewind(current_file)

print("Let's print three lines:")
# Sets a varialbe names current_line to 1
current_line = 1
# Calls the function print_a_line taking two parameters, the current_line (1) and the current_file
print_a_line(current_line, current_file)
# Increments the current_line variable by 1 (2)
current_line += 1
print_a_line(current_line, current_file)
# Increments again the current_line variable by 1 (3)
current_line += 1
print_a_line(current_line, current_file)
