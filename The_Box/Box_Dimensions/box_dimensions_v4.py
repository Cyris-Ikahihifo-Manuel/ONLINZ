# the details function reiterates itself until the customer has input an answer other than an empty string. The function
# first asks the customer through an input statement, addressing them with the noun and subject parameter for context.
# It should then return the customer's answer for use later in the program or for ONLINZ's business such as contacting
# their customers on issues, or asking the customer for an answer with their name.


def details(noun, subject):
    while True:
        answer = input(noun + ', please enter your ' + subject)
        if len(answer) == 0:
            print('error, your answer can\'t be blank')
        else:
            return answer


# this should test the details function

first_name = details('please', 'first name')

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
