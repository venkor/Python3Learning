# this goes in mystuff.py
def apple():
    print("I AM APPLES!")

# This is just a variable
tangerine = "Living reflection of a dream"

class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM A CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)

# three ways to get things from things.
#dict style
# mystuff['apples']
#module style
# mystuff.apples()
# print(mystuff.tangerine)
#class style
# thing = MyStuff()
# thing.apples()
# print(thing.tangerine)
