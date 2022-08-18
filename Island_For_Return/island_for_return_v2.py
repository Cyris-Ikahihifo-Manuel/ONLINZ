# importing random module to get random values for test purposes

from random import randint


# box_volume function has three parameters h, w and d. These parameters are the abbreviation of the box's dimensions
# this is so that the parameters are appropriately named to avoid confusion when other IT programmers in ONLINZ check my
# coding for the program's box by multiplying the box's height, width and depth and then return that value. In the
# complete program, the box's dimensions are collected from the customer who enters the box's dimensions.


def box_volume(h, w, d):
    return h * w * d


# the base_rates function uses both a reiterative statement, conditional statement and 2D list to determine the cost of
# the base rate. The parameters v and c are abbreviations of the intended variables volume and cost in the complete
# program, they're abbreviated to avoid confusion. The 2D list conditions has arrays within it, the first two arrays
# store the minimum and maximum (in that order) values that the parameter v has to be for it to execute the branch
# within the conditional statement. There's a third array in the 2D list conditions, this array stores the cost the
# base rate of the box. In base_rates function, in the conditional statement after parameter v has been put through
# the conditional statement, parameter c experiences an increment of an item in the third array corresponding with the
# same indexes of the two other arrays in the conditional statement, because of the reiterative statement using the
# length of the array conditions[0] it should use all of the other values within the other arrays. It should also return
# the parameter c after experiencing the increment if it goes as expected.


def base_rates(v, c):
    conditions = [[-float('inf'), 6000, 100000], [6000, 100000, float('inf')], [8, 12, 15]]
    for i in range(len(conditions[0])):
        if conditions[0][i] < v <= conditions[1][i]:
            c += conditions[2][i]
    return c


# The 2D list has 2 arrays, these arrays storing the same type of value, with islands_multi[0] storing only strings and
# islands_multi[1]. This is to avoid confusion when storing the variables such as reiterating through one of the arrays
# in the 2D list in the test plan. Each item’s index in islands_multi[0] corresponds with the item in islands_multi[1]
# with the same index. Again, this is to avoid confusion when reiterating through the arrays and using their items.


def islands(location, c):
    islands_multi = [['north island', 'south island', 'stewart island'], [1, 1.5, 2]]
    for i in range(len(islands_multi[0])):
        if location == islands_multi[0][i]:
            c *= islands_multi[1][i]
    return c


# the cost variable is set to 0 because the base rate hasn't been determined yet from the volume of the box or
# multiplying the base_rate on where they're wanting to return their product.

cost = 0

# the variables height, width and depth store the box's dimension, in the complete program the box's dimensions are
# entered by the customer, but in this case the box's dimensions are randomised for test purposes. The print statement is
# to check the box's dimensions and that the volume of the box is correctly calculated. In the complete program, the
# box's dimensions are from inputs from the customer. 

height = randint(5, 100)
width = randint(5, 100)
depth = randint(5, 100)

volume = box_volume(height, width, depth)

print('this box is {}cm tall, {}cm wide and {}cm thick. '
      'This means that the volume of the box is {}^3 cm.'.format(height, width, depth, box_volume(height, width, depth)))

cost = base_rates(volume, cost)

# the program asks the user for input on where they're from, the .strip() and .lower() since conditionals are case
# sensitive the conditional statement should go through all the items in list islands and if the customer's location
# is in the array islands. Then, the cost should be multiplied based on where they're from and exit the conditional
# statement and finally it should display the new cost. The output on here is for test purposes and will be different in
# the complete program.

answer = input('which island are you from?').strip().lower()
islands(answer, cost)
print('that\'ll be ${:.2f}'.format(cost))
