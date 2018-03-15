from sys import argv
script, increment = argv

incrementation = int(increment)

def The_numbers(given_number, incrementation):
    numbers = []
    i = 0
    #while i < given_number:
    for i in range(given_number):
        print(f"At the top i is {i}")
        numbers.append(i)

        #i = i + incrementation
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers

given_number = int(input("How much numbers do you want to fill the table? "))
numbers = The_numbers(given_number, incrementation)
print("The numbers: ")

for num in numbers:
    print(num)
