# this line below imports modules, we're importing the 'sys' module (library)
from sys import argv
# read the WYSS(What you should see) section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

x = input("Daj mnie tu liczbe.")
print(x)
slowo = input("Podaj nazwe kota. \n")
slowo = " " + slowo
print(first + slowo)
