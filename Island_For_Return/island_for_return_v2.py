# importing random module to get random values for test purposes

from random import randint


# box_volume function has three parameters h, w and d. These parameters are the abbreviation of the box's dimensions
# this is so that the parameters are appropriately named to avoid confusion when other IT programmers in ONLINZ check my
# coding for the program's box by multiplying the box's height, width and depth and then return that value. In the
# complete program, the box's dimensions are collected from the customer who enters the box's dimensions.


def box_volume(h, w, d):
    return h * w * d


# these two arrays, islands and base_multiplier have the same amount of items, each item in base_multiplier is the multiplier
# for the item in islands with the same index. In island_for_return, the program should ask the user for where their
# location is and multiply the cost of their box based on where they're from.

islands = ['north island', 'south island', 'stewart island']
base_multiplier = [1, 1.5, 2]

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

# the conditional statement is to determine the base rate of the cost for later. If this goes as expected then the
# program should display that the cost is $8.00 if the volume is 6000cm^3 or less, display $12.00 if the volume of the
# box is greater than 6,000cm^3 but less than or equal to 100,000cm^3 and display $15.00 if the volume of the box is
# greater than 100,000cm^3

if volume <= 6000:
    cost += 8
elif 100000 >= volume > 6000:
    cost += 12
else:
    cost += 15
print('that\'ll be ${:.2f}'.format(cost))

# the program asks the user for input on where they're from, the .strip() and .lower() are used since conditional
# statements are case sensitive the conditional statement should go through all the items in list islands and if the
# customer's location is in the array islands. Then, the cost should be multiplied based on where they're from and exit
# the conditional statement and finally it should display the new cost. The output on here is for test purposes and
# will be different in the complete program.

answer = input('which island are you from?').strip().lower()


if answer == islands[1]:
    cost *= base_multiplier[1]
elif answer == islands[2]:
    cost *= base_multiplier[2]
print('that\'ll be {:.2f}'.format(cost))
