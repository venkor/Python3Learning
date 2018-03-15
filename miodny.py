from os.path import exists
from sys import argv

script, input_file, output_file = argv

#user_sentence = input("Type in a sentence here.\n")
#print(f"Congrats, you've type in:\n{user_sentence}\n")
#print(f"Your sentence is {len(user_sentence)} bytes long.")

#filename = input("Type in the file to copy:\n")

def copy_file(input_file, output_file):
    if (exists(input_file)) == True:
        print(f"The file \"{input_file}\" exists. Copying...")
        indata = (open(input_file)).read()
        out_file = open(output_file, 'w')
        out_file.write(indata)
        out_file.close()
        print(f"Copy finished. Length of {output_file} is {len(output_file)} bytes.")
    else:
        print(f"The file \"{input_file}\" does not exist!\n")
        print("Enter the name of file to copy and hit RETURN or CTRL-C to exit.\n")
        input_file = input("Input file: ")
        copy_file(input_file, output_file)

copy_file(input_file, output_file)
