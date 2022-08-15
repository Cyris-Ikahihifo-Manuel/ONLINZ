# importing the random module to randomise the box's dimensions for test purposes

from random import randint

# box_volume function has three parameters h, w and d. These parameters are the abbreviation of the box's dimensions
# this is so that the parameters are appropriately named to avoid confusion when other IT programmers in ONLINZ check my
# coding for the program's box by multiplying the box's height, width and depth and then return that value. In the
# complete program, the box's dimensions are collected from the customer who enters the box's dimensions.


def box_volume(h, w, d):
    return h * w * d


# in base_rates_v3.py, the base_rates function uses both a reiterative statement, conditional statement and 2D list to
# determine the cost of the base rate, this is more efficient than the conditional statement in the original base_rates.
# Like the original parameters v and c are abbreviations of the intended variables volume and cost in the complete
# program, they're abbreviated to avoid confusion if they were named the same as the global variables. The conditional
# statement in the original function is replaced with a reiterative statement because the conditional statements was
# not only inflexible but inefficient too because if ONLINZ added other base rates for other sizes than programmers
# would've needed to code three more lines of code for each different base rate. In this base rate the person
# programming would only need to add the minimum value of the base rate, the maximum value of the base rate and the
# cost of the conditions while still executing the same purpose with the same amount of lines. The 2D list conditions
# has arrays within it, the first two arrays store the minimum and maximum (in that order) values that the parameter v
# has to be for it to execute the branch within the conditional statement. There's a third array in the 2D list
# conditions, this array stores the cost the base rate of the box. In base_rates function, in the conditional statement
# after parameter v has been put through the conditional statement, parameter c experiences an increment of the third
# array corresponding with the same indexes of the two other arrays in the conditional statement, because of the
# reiterative statement using the length of the array conditions[0] it should use all of the other values within the
# other arrays. It should also return the parameter c after experiencing the increment if it goes as expected.


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
# they're returning the box from. The print statements are to check that the program is running as expected

cost = 0

height = randint(5, 100)
width = randint(5, 100)
depth = randint(5, 100)

volume = box_volume(height, width, depth)
print('the box is {} cm tall, {} cm wide and {} cm thick so the volume is {}cm^3'.format(height, width, depth, volume))

cost = base_rates(volume, cost)
print('that\'ll be ${:.2f}'.format(cost))
