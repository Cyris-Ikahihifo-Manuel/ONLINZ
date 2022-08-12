# importing the random module to randomise the box's dimensions for test purposes

from random import randint

# box_volume function has three parameters h, w and d. These parameters are the abbreviation of the box's dimensions
# this is so that the parameters are appropriately named to avoid confusion when other IT programmers in ONLINZ check my
# coding for the program's box by multiplying the box's height, width and depth and then return that value. In the
# complete program, the box's dimensions are collected from the customer who enters the box's dimensions.


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
print('the box is {} cm tall, {} cm wide and {} cm thick so the volume is {}cm^3'.format(height, width, depth, volume))

# if this goes according to the test plan the conditional statement should execute the first branch if the volume of the
# box is less than or equal to 6,000 cm^3, making the base rate $8.00 and stored in the variable cost.
# It should also execute the second branch if the volume of the box is greater than 6,000cm^3 but less than or equal to
# 100,000cm^3, making the base rate $12.00 and stored in the variable cost. And finally, it should execute the final
# branch if the volume of the box is greater than 100,000cm^3, making the base rate $15.00 and stored in the variable
# cost. It should do all of this without issues such as crashing for invalid values or bugs. If im right, then <
# represents less than whereas > represents greater than, <= represents less than or equal to whereas >= represents
# greater than or equal to and == represents equal to. The print statements within the branches in the conditional
# statements are for test purposes only and will be changed later in the complete program (if this version of base_rates
# makes it into the complete program).

if volume <= 6000:
    print('that\'ll be $8.00')
    cost = cost + 8
elif 100000 > volume > 6000:
    print('that\'ll be $12.00')
    cost = cost + 12
else:
    print('that\'ll be $15.00')
    cost = cost + 15
