# importing the random module to randomise the box's dimensions for test purposes

from random import randint

# box_volume function has three parameters h, w and d. These parameters are the abbreviation of the box's dimensions
# this is so that the parameters are appropriately named to avoid confusion when other IT programmers in ONLINZ check my
# coding for the program's box by multiplying the box's height, width and depth and then return that value. In the
# complete program, the box's dimensions are collected from the customer who enters the box's dimensions.


def box_volume(h, w, d):
    return h * w * d


# in base_rates_v2.py theres a function called base_rates. Firstly, its named base_rate appropriately
# its used for. Secondly, the parameter v is the abbreviation of volume and c is the abbreviation of cost, they're
# abbreviated to avoid confusion mixing up local and global variables. Now, the purpose of this function is to take the
# parameter v, input it through conditional statements and if it goes according to the test plan, the parameter c
# experiences an increment of 8 if parameter v is less than or equal to 6000, parameter c experiences an increment of 12
# if parameter v is greater than 6000 but less than or equal to 100000 and then parameter c experiences an increment of
# 15 if parameter v is greater than 100,000. Finally, according to the test plan, it should return parameter c because
# parameter c is the parameter being changed whereas parameter v is being used for conditional statements. base_rates
# function doesn't have print statements within the branches in the conditional statement because they were there
# originally for test purposes to check if it worked properly.


def base_rates(v, c):
    if v <= 6000:
        c += 8
    elif 100000 >= v > 6000:
        c += 12
    else:
        c += 15
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
