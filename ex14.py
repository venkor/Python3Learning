#Imports the sys module (library)
from sys import argv
#requires 2 arguments to run
script, user_name, nickname = argv
#Our new prompt looks like this now, it's a string variable with two ">" and a space
prompt = '>> '
#Some little chit-chat with the user - using formatting to input the variables given when running script
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Heard, that they call you {nickname} in da hood, right?")
#Asking some additional information, using formatting
print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)
#printing the summary of what have been gathered from the user. 3 quotes are used with formatting.
print(f"""
Alright, so you say {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have {computer} computer. Nice.
""")
