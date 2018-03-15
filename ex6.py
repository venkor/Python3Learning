# setting a variable type_of_people to 10
type_of_people = 10
# setting a new formatted string variable 'x' which conatins text and variable type_of_people inside of it.
x = f"There are {type_of_people} types of people."
# setting new string named binary
binary = "binary"
# setting new string named do_not
do_not = "don't"
# settign new string named 'y' which contains text and two variables inside named 'binary' and 'do_not'
y = f"Those who know {binary} and those who {do_not}."
# prints out the variable x which is a formatted string
print(x)
# prints out the variable y which is a formatted string
print(y)
# prints out a formatted strings and a variable inside, which is also a formatted string 'x'
print(f"I said: {x}")
# prints out a formatted strings and a variable inside, which is also a formatted string 'y'
print(f"I also said: '{y}'")
# setting new boolean variable named 'hilarious' to False
hilarious = False
# setting new string variable named 'joke_evaluation' which takes one formatting parameter
joke_evaluation = "Isn't that joke so funny?! {}"
# prints out the formatted string joke_evaluation with format() function used and 'hilarious' boolean value passed to it
print(joke_evaluation.format(hilarious))
# setting a new string variable named 'w'
w = "This is the left side of..."
# setting a new string variable named 'e'
e = "a string with a right side."
#prints out the contatenation of two string variables 'w' and 'e'
print(w + e)
