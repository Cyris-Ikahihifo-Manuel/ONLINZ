# box_dimension function 1.0 should crash for invalid values (such as strings or floats) and display no other output
# for out of bound values (-1 or 101). It also shouldn't reiterate the lines of code within the function.


def box_dimension(message):
    answer = int(input(message))
    if 5 <= answer <= 100:
        return answer


# the box_dimension function being tested

height = box_dimension('enter box\'s height in cm')
width = box_dimension('enter box\'s width in cm')
depth = box_dimension('enter box\'s depth in cm')

# the box's dimensions being output

print('the box is {} cm tall, {} cm wide and {} cm thick')
