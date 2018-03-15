# Prints out a string
print("Mary had a little lamb.")
#name = "bob"
# Prints out a formated string, where the brackets takes the directly given string parameter 'snow'
print("Its fleece was white as {}".format('snow.')) # replaced 'snow' with variale 'name'
# Prints another sentence string
print("And everywhere that Mary went.")
# Prints out ten times a dot. It multiplies the amount of string to be printed.
print("." * 10) # what'd that do?
#below end(1-12) variables are new string declarations - it all sums up to be a Cheese Burger
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = '' at the end. try removing it to see what happens -> If I remove the '' quotes and try to run the script - it fucks up and throws and error, because a blank char (space) is a char and should be in brackets like any other string. That's the string formatting in python I guess.
# Prints out a sum of string variables and additionaly a one newly decaled named 'end' which is set to a string which contais a single blank char - space. It prints out the word Cheesse <-space here.
print(end1 + end2 + end3 + end4 + end5 + end6 + end = ' ')
# Prints out a sum of string variables from end 7 to end 12, which gives us the word 'Burger'
print(end7 + end8 + end9 + end10 + end11 + end12)
