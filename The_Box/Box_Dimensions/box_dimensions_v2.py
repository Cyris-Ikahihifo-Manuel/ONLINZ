# box_dimension function 2.0 should ask the user for input, displaying the message parameter for context. The
# box_dimension function shouldn't  crash for invalid values such as floats or strings and instead display the
# error_message parameter. It should also display the error_message parameter for out of bound values such as
# numbers less than 5 or more than 100. The function should also reiterate itself until the user has input an integer
# equal to or more than 5 and equal to or less than 100 and return that value the user has entered.


def box_dimension(message, error_message):
    while True:
        try:
            print()
            answer = int(input(message))
            if 5 <= answer <= 100:
                return answer
            else:
                print()
                print(error_message)
        except ValueError:
            print()
            print(error_message)


# the box_dimension function being tested

height = box_dimension('enter box\'s height in cm', 'error, height of box must be a whole number between 5 and 100 cm')
width = box_dimension('enter box\'s width in cm', 'error, width of box must be a whole number between 5 and 100 cm')
depth = box_dimension('enter box\'s depth in cm', 'error, depth of box must be a whole number between 5 and 100 cm')

# the box's dimensions being output

print('the box is {} cm tall, {} cm wide and {} cm thick'.format(height, width, depth))
