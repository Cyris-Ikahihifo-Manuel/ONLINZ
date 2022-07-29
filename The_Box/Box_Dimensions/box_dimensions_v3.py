# box_dimension function 3.0 shouldn't crash for invalid values such as floats or strings and instead display the
# dimension formatted in the statement "error, the box's {} must be between 5 to 100 cm".


def box_dimension(dimension):
    while True:
        try:
            answer = int(input('enter your box\'s {} in cm'.format(dimension)))
            if 5 <= answer <= 100:
                return answer
            else:
                print('error, the box\'s {} must be between 5 to 100 cm'.format(dimension))
        except ValueError:
            print('error, the box\'s {} must be entered in whole numbers'.format(dimension))


# the box_dimension function being tested

height = box_dimension('height')
width = box_dimension('width')
depth = box_dimension('depth')

# the box's dimensions being output

print('the box is {} cm tall, {} cm wide and {} cm thick'.format(height, width, depth))
