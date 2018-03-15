from sys import argv

script, filename = argv
# We can skip the lines 5-10,so I'm going to comment-out the code.
# print(f"We're going to erase {filename}.")
# print("If you don't want that, hi CTRL-C (^C).")
# print("If you do want that, hit RETURN.")

# input("?")

print("Opening the file...")
target = open(filename, 'w')
#Truncating not needed when file is open with the parameter 'w', however it won't be able to truncate or save the file without the parameter, because the file won't be opended in writing mode
#print("Truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you for the three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")
# We can use only one target.write (use the write() method on targer variable) and write all the strings we want to, appending them together wth '+' sign
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
# We can't forget about closing the file. It's like 'File>Save...'
print("And finally, we close it.")
target.close()
