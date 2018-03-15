# The IF statement checks if the statement is True and runs instructions underneath
# The code under the IF statement requires 4 spaces in Python, becaue of the syntax to tell Python than instructions underneath are assigned to the partiucual IF statemnet.
# If it's not indented the code fail and throw an error: expected an indented block. We can use 'pass' to fill that expected block.
people = 20
cats = 30
dogs = 15


if people < cats and (cats >= dogs):
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if  people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
