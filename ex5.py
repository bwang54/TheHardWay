my_name = "Zed A. Shaw"
my_age = 35 # not a lie
my_height = 74 # inches
my_heightcm = my_height * 2.54 # cm
my_weight = 180 # lbs
my_weightkg = my_weight * 0.453592 # kg
my_eyes = "Blue"
my_teeth = "White"
my_hair = "brown"

print "Let's talk about %s." % my_name
print "He is %d inches or %d centimeters tall." % (my_height, my_heightcm)
print "He is %d pounds or %d kgs heavy." % (my_weight, my_weightkg)
print "Acturally that's not too heavy."
print "He is got %s hair and %s eyes." % (my_hair, my_eyes)
print "His teeth are usually %s depending on the coffee." % my_teeth

# This line is tricky, try to get it exactly right.
print "If I get %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight
)
