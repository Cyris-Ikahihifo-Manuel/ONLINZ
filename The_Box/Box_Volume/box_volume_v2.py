# importing random module to randomise values

import random

# box_volume function 2.0 has three parameters h, w and d. These parameters are the abbreviation of the box's dimensions.
# The parameters defining box_volume are abbreviated later so that in the complete program's coding there is less
# confusion programming the complete program. But in box_volume function 2.0 it should calculate the volume of
# the customer's box by multiplying the box's height, width and depth and then return that value. There's no volume
# variable like in box_dimension 1.0 function because we could return calculations, as well as multiple variables at
# once, so instead of calculating the volume and then storing it in a variable, box_volume function 2.0 returns the
# volume of the box in a single line.


def box_volume(h, w, d):
    return h * w * d


# program being tested

# importing random module to randomise values

import random

# box_volume function 2.0 has three parameters h, w and d. These parameters are the abbreviation of the box's dimensions
# that were asked by us from my superiors in ONLINZ. In the box_volume function it should calculate the volume of the
# customer's box by multiplying the box's height, width and depth and then return that value. In the complete program,
# the box's dimensions are collected from the customer who enters the box's dimensions.


def box_volume(h, w, d):
    return h * w * d


# program being tested

height = random.randint(5, 100)
width = random.randint(5, 100)
depth = random.randint(5, 100)
print('this box is {}cm tall, {}cm wide and {}cm thick. '
      'This means that the volume of the box is {}^3 cm.'.format(height, width, depth, box_volume(height, width, depth)))

print('this box is {}cm tall, {}cm wide and {}cm thick. '
      'This means that the volume of the box is {}^3 cm.'.format(height, width, depth, box_volume(height, width, depth)))
