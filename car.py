cars = 100
space_in_a_car = 4.0
drivers =30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are" ,cars, "cars available"
print "There are only",drivers, "driver acailable"
print "There will be",cars_not_driven

i = 5
j = 8
x = 9

print "the answer is",i * j
print x/i
print i-j < x
print i-j> j
print x % j