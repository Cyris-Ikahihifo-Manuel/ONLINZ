# the details function reiterates itself until the customer has input an answer other than an empty string. The function
# first asks the customer through an input statement, addressing them with the noun and subject parameter for context.
# It should then return the customer's answer for use later in the program or for ONLINZ's business such as contacting
# their customers on issues, or asking the customer for an answer with their name.


def details(noun, subject):
    while True:
        print()
        answer = input(noun + ', please enter your ' + subject)
        if len(answer) == 0:
            print()
            print('error, your answer can\'t be blank')
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
            answer = int(input(noun + ', please enter your ' + subject))
            return answer
        except ValueError:
            print()
            print('error, phone number must be in numbers')


# this should test the details function

first_name = details('please', 'first name').capitalize()

surname = details(first_name, 'surname')

address = details(first_name, 'address')

phone_no = int_details(first_name, 'phone number')

# this checks that the program is working as expected

print('your first name is {}, your surname is {}, your address is {} '
      'and your phone number is {}'.format(first_name, surname, address, phone_no))
