# importing random module to randomise values

import random

# box_volume function 1.0 has three parameters height, width and depth. In the box_volume function it should calculate
# the volume of the customer's box by multiplying the box's height, width and depth, store the volume of the box in a
# variable called volume and then return volume. The import random module is there because in the complete program,
# the box's dimensions are collected from the customer who enters their box's dimensions.


def box_volume(height, width, depth):
    volume = height * width * depth
    return volume


# program being tested

h = random.randint(5, 100)
w = random.randint(5, 100)
d = random.randint(5, 100)
print('this box is {}cm tall, {}cm wide and {}cm thick. '
      'This means that the volume of the box is {}^3 cm.'.format(h, w, d, box_volume(h, w, d)))
