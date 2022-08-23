# box_dimension function 4.0 is more aesthetically pleasing than box_dimensions 3.0, printing spaces between asking
# for input and displaying output, box_dimension 4.0 should still display the dimension parameter formatted in the
# statement "enter your box's {} in cm". The function should also still shouldn't crash for invalid values such as
# floats or strings and instead display the dimension formatted in the statement "error, the box's {} must be entered
# in whole numbers". The box_dimension function should also display the dimension formatted in the statement "error, the
# box's {} must be entered a whole number between 5 to 100". The box_dimension function should also reiterate itself
# until the user has entered an integer equal to or greater than 5 or equal to or less than 100 and return the value
# that the user has entered.


def box_dimension(dimension):
    while True:
        try:
            print()
            answer = int(input('Enter your box\'s {} in cm'.format(dimension)))
            if 5 <= answer <= 100:
                return answer
            else:
                print()
                print('Error, the box\'s {} must be entered a whole number between 5 to 100'.format(dimension))
        except ValueError:
            print()
            print('Error, the box\'s {} must be entered in whole numbers'.format(dimension))


# the box_dimension function being tested

height = box_dimension('height')
width = box_dimension('width')
depth = box_dimension('depth')

# the box's dimensions being output

print('the box is {} cm tall, {} cm wide and {} cm thick'.format(height, width, depth))
