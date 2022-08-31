# he details function reiterates itself until the customer has input an answer other than an empty string. The function
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

surname = details(first_name, 'surname')

address = details(first_name, 'address')

phone_no = details(first_name, 'phone number')

# this checks that the program works as expected according to the test plan

print('your first name is {}, your surname is {}, your address is {} '
      'and your phone number is {}'.format(first_name, surname, address, phone_no))
