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
