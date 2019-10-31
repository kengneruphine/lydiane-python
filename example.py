#more work on printing
x = "There are %d types of people." %10 # %10 replaces %d
binary = "binary"
do_not = "don't"
y= "Those who know %s and those who %s." %(binary,do_not) # join both word in the sentence

print x
print y

print "I said : %r." %x # print x with single quotes on it
print "I also said: '%s'. " %y  # print y

hilarious = False
joke_evaluation = "Isn't that jole so funny?! %r"
print joke_evaluation % hilarious # concatenate two variables

w = "This is the left side of..."
e = "a string with a right side."

print  w + e # join or concatenate the two string