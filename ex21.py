def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply_much(a, b):
    print(f"MULTIPLYING {a} * {b} * ({b} + {a})")
    sum = a * b * (b + a)
    return sum

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")
my_age = int(input("Enter your age\n"))
age = add(my_age, 5)
height = substract(78, 4)
weight = multiply(90, 2)
my_iq = float(input("Enter your IQ\n"))
iq = divide(my_iq, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))
# what = add(35, -4426) = -4391 - yeah, I can do it by hand.
print("That becomes: ", what, "Can you do it by hand?")

# My formula: (204/4)*12) + 24 - (34/2)
what2 = add(multiply(divide(204, 4), 12), substract(24, divide(34,2)))
print("That what2 becomes: ", int(what2)) # Throwing this on int works
