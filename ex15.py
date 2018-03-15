# Importing argv module from sys package - I think I've named it the right way here for the first time :)
from sys import argv
# taking 1 agument when running the script
script, filename = argv
# declaration of 'txt' variable and opening the "filename" argument given when running this script.
txt = open(filename)
# Prints out the "filename" variable given as an argument when running the script
print(f"Here's your file {filename}:")
# running the read() method on the 'txt' variable which is assigned to the open(filename) function
print(txt.read())
# It's important to close() file when we're done with them
txt.close()
# printing a little statement to the user to write the desired filename
print("Type the filename again.")
# declaration of a new varable that will hold the new filename from user input. String "> " is given as incentive
file_again = input("> ")
# declaration of a new variable which opens the filename given in file_again variable
txt_again = open(file_again)
# prints out the text_again variable by using the read() method on opened file.
print(txt_again.read())
# It's important to close() files when we're done with them
txt_again.close()
#filename used for this excersize is: ex15_sample.txt
