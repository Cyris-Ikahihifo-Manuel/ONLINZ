# importing the random module to randomise the box's dimensions for test purposes

from random import randint

# box_volume function has three parameters h, w and d. These parameters are the abbreviation of the box's dimensions
# this is so that the parameters are appropriately named to avoid confusion when other IT programmers in ONLINZ check my
# coding for the program's box by multiplying the box's height, width and depth and then return that value. In the
# complete program, the box's dimensions are collected from the customer who enters the box's dimensions.


def box_volume(h, w, d):
    return h * w * d


# in base_rates_v3.py function


def base_rates(v, c):
    conditions = [[-float('inf'), 6000, 100000], [6000, 100000, float('inf')], [8, 12, 15]]
    for i in range(len(conditions[0])):
        if conditions[0][i] < v <= conditions[1][i]:
            c += conditions[2][i]
    return c


# here is where the program randomises the box's dimensions for test purposes and later displays the box's dimensions,
# this is to make sure that the calculation of the volume of the box is correct. The variable is also being stored in a
# variable called cost, this variable stores the base rate of the box for the test, in the complete program, this
# variable (cost) stores the information of the total cost depending on the customer's volume of the box and where
# they're returning the box from.

cost = 0

height = randint(5, 100)
width = randint(5, 100)
depth = randint(5, 100)

volume = box_volume(height, width, depth)
print('the box is {} cm tall, {} cm wide and {} cm thick so the volume is {}cm^3'.format(height, width, depth, volume))

cost = base_rates(volume, cost)
print('that\'ll be ${:.2f}'.format(cost))
