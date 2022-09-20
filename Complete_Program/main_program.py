# the decorations function makes it so that the program displays a certain message 'decorated'


def decorations(message, decoration):
    print()
    print(decoration * (len(message) + 6))
    print((decoration * 3) + message + (decoration * 3))
    print(decoration * (len(message) + 6))


# the message function uses two print statements. One that's blank and the other that prints the parameter message.
# This function


def text(message):
    print()
    print(message)


# box_volume function 2.0 has three parameters h, w and d. These parameters are the abbreviation of the box's dimensions
# that were asked by us from my superiors in ONLINZ. In the box_volume function it should calculate the volume of the
# customer's box by multiplying the box's height, width and depth and then return that value. In the complete program,
# the box's dimensions are collected from the customer who enters the box's dimensions.


def box_volume(h, w, d):
    return h * w * d


# in base_rates_v3.py, the base_rates function uses both a reiterative statement, conditional statement and 2D list to
# determine the cost of the base rate, this is more efficient than the conditional statement in the original base_rates.
# Like the original parameters v and c are abbreviations of the intended variables volume and cost in the complete
# program, they're abbreviated to avoid confusion if they were named the same as the global variables. The conditional
# statement in the original function is replaced with a reiterative statement because the conditional statements was
# not only inflexible but inefficient too because if ONLINZ added other base rates for other sizes than programmers
# would've needed to code three more lines of code for each different base rate. In this base rate the person
# programming would only need to add the minimum value of the base rate, the maximum value of the base rate and the
# cost of the conditions while still executing the same purpose with the same amount of lines. The 2D list conditions
# has arrays within it, the first two arrays store the minimum and maximum (in that order) values that the parameter v
# has to be for it to execute the branch within the conditional statement. There's a third array in the 2D list
# conditions, this array stores the cost the base rate of the box. In base_rates function, in the conditional statement
# after parameter v has been put through the conditional statement, parameter c experiences an increment of the third
# array corresponding with the same indexes of the two other arrays in the conditional statement, because of the
# reiterative statement using the length of the array conditions[0] it should use all of the other values within the
# other arrays. It should also return the parameter c after experiencing the increment if it goes as expected.


def base_rates(v, c):
    conditions = [[-float('inf'), 6000, 100000], [6000, 100000, float('inf')], [8, 12, 15]]
    for i in range(len(conditions[0])):
        if conditions[0][i] < v <= conditions[1][i]:
            c += conditions[2][i]
    return c


# the details function reiterates itself until the customer has input an answer other than an empty string. The function
# first asks the customer through an input statement, addressing them with the noun and subject parameter for context.
# It should then return the customer's answer for use later in the program or for ONLINZ's business such as contacting
# their customers on issues, or asking the customer for an answer with their name.


def details(noun, subject):
    while True:
        print()
        answer = input(noun + ', enter your ' + subject).strip()
        if len(answer) == 0:
            decorations('Error, your {} can\'t be blank.'.format(subject), '!')
        else:
            return answer


# the int_details function reiterates itself until the customer has input a whole number. The function first asks the customer
# through an input statement, addressing them with the noun and subject parameter for context. It should then return the
# customer's answer for use later in the program or for ONLINZ's business such as contacting their customers on issues,
# or asking the customer with their name.


def int_details(noun, subject):
    while True:
        try:
            print()
            answer = int(input(noun + ', enter your ' + subject))
            return answer
        except ValueError:
            decorations('Error, your {} must be entered in whole numbers.'.format(subject), '!')


# box_dimension function 4.0 is more aesthetically pleasing than box_dimensions 3.0, printing spaces between asking
# for input and displaying output, box_dimension 4.0 should still display the dimension parameter formatted in the
# statement "enter your box's {} in cm". The function should also still shouldn't crash for invalid values such as
# floats or strings and instead display the dimension formatted in the statement "error, the box's {} must be entered
# in whole numbers". The box_dimension function should also display the dimension formatted in the statement "error, the
# box's {} must be entered a whole number between 5 to 100". The box_dimension function should also reiterate itself
# until the user has entered an integer equal to or greater than 5 or equal to or less than 100 and return the value
# that the user has entered.


def box_dimension(noun, dimension):
    while True:
        try:
            print()
            answer = int(input('{}, enter your box\'s {} in cm'.format(noun, dimension)))
            if 5 <= answer <= 100:
                return answer
            else:
                decorations('Error, the box\'s {} must between 5 and 100 cm, {}'.format(dimension, noun), '!')
        except ValueError:
            decorations('Error, the box\'s {} must be entered in whole numbers, {}'.format(dimension, noun), '!')


islands_multi = {'north island': 1, 'south island': 1.5, 'stewart island': 2}

cost = 0

# this should test the details function in the functions

contacts = []
while True:
    first_name = details('please', 'first name').capitalize()
    surname = details(first_name, 'surname').capitalize()
    address = details(first_name, 'address')
    phone_no = int_details(first_name, 'phone number')

    height = box_dimension(first_name, 'height')
    width = box_dimension(first_name, 'width')
    depth = box_dimension(first_name, 'depth')

    volume = box_volume(height, width, depth)
    text('{}cm x {}cm x {}cm = {}cm^3'.format(height, width, depth, volume))

    cost = base_rates(volume, cost)
    decorations('The box\'s volume is {} cm^3 so the base rate will ${:.2f}, {}'.format(volume, cost, first_name), '~')

    not_finished = True
    while not_finished:
        decorations('Locations in New Zealand', '~')
        print()
        for island in islands_multi.keys():
            print(island.capitalize())
        location = details(first_name, 'location')
        for island in islands_multi.keys():
            if location == island:
                cost *= islands_multi[island]
                not_finished = False

    decorations('Based on your location, that\'ll be ${:.2f}, {}'.format(cost, first_name), '-')
    contacts.append([first_name, surname, address, phone_no, volume, cost, location])
