# Defines our function names cheese_and_crackers which takes two arguments (cheese_count and boxes_of_crackers)
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # The function just prints out the variables given in funny senteces.
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# We're calling the cheese_and_crackers function giving it directly the 2 arugments as numbers
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)


print("OR, we can use variables from our script:")
# We're creating two variables, amount_of_cheese and amount_of_crackes and assigning numbers to them.
amount_of_cheese = 10
amount_of_crackes = 50
# We're running the cheese_and_crackers function and we're passing our variables(amount_of_cheese, amount_of_crackes) as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackes)


print("We can even do math inside too:")
# When using the function cheese_and_crackers we can even pass staight the math results as arguments
cheese_and_crackers(10 + 20, 5 + 6)

# When caling the function cheese_and_crackers we can combine variales and numbers with math and pass the results are arguments
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackes + 1000)

def fill_yerba_mate(pot, weed, straw):
    print(f"Let's make a yerba mate with this {pot}, this {weed} and slurp it up with {straw}.")

def fill_yerba_poor(pot, weed):
    print(f"We're quite poor but we want the kick. Let's combine this {pot} and {weed} and slurp it up right from the {pot}.")

def fill_yerba_rambo_style(weed):
    print(f"We just chew raw {weed}, like real men.")
def fill_yerba():
    print("OFC")
yerba_weed = "Pajarito"
yerba_weed2 = "CBSE"
def yerba_weed_types(*args):
    yerba_weed, yerba_weed2 = args
    print(f"In stock we have now: {yerba_weed}, {yerba_weed2}")

fill_yerba_mate("matero made from palo santo", yerba_weed, "classic Bombilla")
fill_yerba_poor("ceramic matero", "cheap " + yerba_weed)
fill_yerba_rambo_style(yerba_weed)
fill_yerba()
yerba_weed_types(yerba_weed, yerba_weed2)
