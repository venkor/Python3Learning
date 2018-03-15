# defines a new formatted strings which contains blank characters (spaces) and 4 places for formatting
formatter = "{} {} {} {}"
# Prints out the formatter formated variable with passing integer variables in the formatting brackets - 1st bracket -> 1st given variable
print(formatter.format(1, 2, 3, 4))
# Prints out the formatter formatted string variable with passing four strings as formatting variables
print(formatter.format("one", "two", "three", "four"))
# Prints out the formatter formatted string variable with passing four boolean variables as formatting variables
print(formatter.format(True, False, False, True))
# Prints out the formatter formatted string variable with passing four times the formatted sting variable named "formatter". Some kind of recurency going here :P
print(formatter.format(formatter, formatter, formatter, formatter.format(formatter, formatter, formatter, formatter))) # slightly modified, long story short - we must go deeper...
# Prints out the formatter formatted string variable with passing four strings, but gived in different code formatting - looks pretier in the editor, but only there ;)
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
