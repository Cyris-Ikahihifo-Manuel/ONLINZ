# importing the random module to randomise the box's dimensions for test purposes

from random import randint

# box_volume function 2.0 has three parameters h, w and d. These parameters are the abbreviation of the box's dimensions
# that were asked by us from my superiors in ONLINZ. In the box_volume function it should calculate the volume of the
# customer's box by multiplying the box's height, width and depth and then return that value. In the complete program,
# the box's dimensions are collected from the customer who enters the box's dimensions.


def box_volume(h, w, d):
    return h * w * d


# here is where the program randomises the box's dimensions for test purposes and later displays the box's dimensions,
# this is to make sure that the calculation of the volume of the box is correct. The variable is also being stored in a
# variable called cost, this variable stores the base rate of the box

cost = 0

height = randint(5, 100)
width = randint(5, 100)
depth = randint(5, 100)

volume = box_volume(height, width, depth)

# if this goes according to the test plan the conditional statement should execute the first branch if the volume of the
# box is less than or equal to 6,000 cm^3, making the base rate $8.00 and stored in the variable cost.
# It should also execute the second branch if the volume of the box is greater than 6,000cm^3 but less than or equal to
# 100,000cm^3, making the base rate $12.00 and stored in the variable cost. And finally, it should execute the final
# branch if the volume of the box is greater than 100,000cm^3, making the base rate $15.00 and stored in the variable
# cost. It should do all of this without issues such as crashing for invalid values or bugs.

if volume <= 6000:
    cost += 8
elif 6000 > volume <= 100000:
    cost += 12
else:
    cost += 15
