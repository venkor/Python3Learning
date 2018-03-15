from sys import argv

script, file_to_read = argv

print(f"Going to write down the file you've chosen: {file_to_read} :\n")
open_file = open(file_to_read)
print(open_file.read())
