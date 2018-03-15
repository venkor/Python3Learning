from sys import argv

script, my_file = argv


data = open(my_file)
indata = data.read()
print(f"Let's check the length of the file {my_file}.")
print(f"The length of the {my_file} is {len(indata)} bytes")
data.close()
