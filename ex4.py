#Number of cars we have
cars = 100
#The total space we have in a single car
space_in_a_car = 4.0
#The total amount of drivers we currently have
drivers = 30
#The amount of passangers we need to handle
passengers = 90
#The number of free (not used) cars we have left
cars_not_driven = cars - drivers
#The number of cars that are in use (typically the number of drivers)
cars_driven = drivers
#The capapcity of all the cars - how passangers we can transport at once using all our cars
carpool_capacity = cars_driven * space_in_a_car
#The avarage number of passangers in a single car to get all the available cars running
avarage_apssengers_per_car = passengers / cars_driven

#Prints info about how many cars we currently have
print("There are", cars, "cars available.")
#Prints how much drivers we have
print("There are only", drivers, "drivers available.")
#Prints the amount of not used cars today
print("There will be", cars_not_driven, "empty cars today.")
#Prints the info of how much we people we can transport today
print("we can transport", carpool_capacity, "people today.")
#Prints the amount of passengers we have to handle today
print("We have", passengers, "to carpool today.")
#Prints the avarage number of passengers we need to put in a single available car
print("We need to put about", avarage_apssengers_per_car, "in each car.")
