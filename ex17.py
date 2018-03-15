# I can make the script in one line by separating each instruction with ";"
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}, hit RETURN to continue or CTRL-C to abort.")
input()
#We could do these two on one line, how?
#in_file = (open(from_file)).read()
in_file = open(from_file)
indata = in_file.read()
#input("test")
#print(f"The input file is {len(indata)} bytes long")

#print(f"Does the output file exist? {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

#out_file.close()
in_file.close()





#Jescze raz to cwiczenie zrobic, nie ogarniam na galy i na banie.spac. jest 00:21 w piatek w sumie juz. branoc.
