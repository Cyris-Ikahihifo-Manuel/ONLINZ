# box_dimension function 1.0 should crash for invalid values (such as strings or floats) and displays no other output
# for out of bound values (-1 or 101). It also shouldn't reiterate the lines of code within the function.
# Also the input from the user should be returned if the user has entered an integer equal to or more than 5 or equal
# to or less than 100.


def box_dimension(message):
    answer = int(input(message))
    if 5 <= answer <= 100:
        return answer


# the box_dimension function being tested

height = box_dimension('enter box\'s height in cm')
width = box_dimension('enter box\'s width in cm')
depth = box_dimension('enter box\'s depth in cm')

# the box's dimensions being output

print('the box is {} cm tall, {} cm wide and {} cm thick'.format(height, width, depth))
