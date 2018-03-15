#list of used symbols
print() #prints out to terminal what's inside the parenthesis
"" # double parenthesis
'' # single parenthesis
# # An octothorpe, pound is used to write comments in code
+ # plus, addition - used for math or string addition
- # minus - used for substraction
/ # used for devision
* # asterisk, used as mutliplication or sometimes a wildcard
% # percent, used as modulo (rest from devision)
< # less-than, used for comparsion, returns an boolean value (True or False)
> # greater-than, used for comparion, returns an boolean value (True or False)
<= # less-than-equal, used for comparsion, returns an boolean value (True or False)
>= # greater-than-equal, used for comparion, returns and boolean value (True or False)
print("Is it greater?", 5 > -2) # comma separates each variable ( this will print a string and the boolean True value of the comparsion result)
cars = "blue" # variables, the "=" assigns a value to the variable. First appearance of a variable in code usually is a declaration
red_car = 2 # a variable can't start from a number, only characters and underscores are good to go (_)
print(f"This is a {car}") # 'f' is used to format a print output, it gives us the ability to put variables in our printing output in much easier way
x = f"There are only {red_car} red cars here" # we can assign a formatted string to a variable
koko = "Hey, this is: {}"; print(koko.format("Mario!")) # We can leave a blank {}. Also we use ; to separate code lines. The "Mario!" string gets to the first free {}
formatter = "{} {} {} {}"; print(formatter.format(1,formatter,"lol",False)) # same as above
print("""
blabla
blankbla
Toast
""")    # triple qoutes are used to nice text formatting. It will get printes as it looks in the code. Nice.
#\ # usually used to escape characters, below list of escape characters
print("\\") # Backslash \
print("\'") # Single quote(')
print("\"") # Double quote(")
print("\a") # ASCII bell (BEL)
print("\b") # ASCII backspace (BS)
print("\f") # ASCII formfeed (FF)
print("\n") # ASCII linefeed (LF)
print("\n{name}") # Character named name in the Unicode database (Unicode only)
print("\r") # Carriage Return (CR)
print("\t") # Horizontal Tab (TAB)
print("\uxxxx") # Character with 16-bit hex value xxxx (u" string only)
print("\Uxxxxxxxx") # Character with 32-bit hex value xxxxxxxx (U" string only)
print("\v") # ASCII vertical tab (VT)
print("\ooo") # Character with octal value ooo
print("\xhh") # Character with hex value hh
age = input() # Requests input from the user and assigns it to the variable age
surname = input("What is your surname?") # Same as above, but we can print a string inside the input()
from sys import argv # on top of each script. Imports argv module from python sys library
script, frist, second, third = argv # unpacts given parameters when running scripts to variables from left to right.
prompt = 'hey '; yoyo = input(prompt) # we can use a variable inside the input() function
txt = open(filename) # opens the file given - there are different open() options
txt = open(filename, 'w') # opens the file in writing mode
# 'r' - read mode which is used when the file in only being read
# 'w' - write mode which is used to edit and write new information to the file (any existing giles with the same name will be erased when this mode is activated)
# 'a' - appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the amended to the amended
# 'r+' - Special read and write mode, which is used to handle both actions when working with a file
txt.read() # reads the file given, now we can print it out
txt.close() # We should  close all the files that we're done with. It's a good practice. It's like File>Save...
txt.readline # Reads just one line of a text file.
txt.truncate # Empties the file.
txt.write('stuff') # Writes "stuff" to the file.
txt.seek(0) # Move the read/write location to the beginning of the file ( to the 0 byte )
len(indata) # returns the length of a text file in number of bytes, first the indata variable had to read the input file with read()
exists(my_file) # Checks if the my_file exists - return a boolean True or False value
from os.path import exists # imports the exists module  from os.path python library
def print_three(*args): # defines a new function, *args gets all the given arguments and assigns them to varaible, just like using the script with arguments
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")
    sum = arg2 + arg3
    return sum # a function can return something that can be assigned to a variable, a value from a function
print_three("lol", 3 + 2, cars) # calls, runs, use of the function print_three with two arguments given.
# The call of the function can take different kinds of arguments: variables, results of math, strings, other functions aswell.
a_variable += 2 # Is the same as a_variable = a_variable + 2
