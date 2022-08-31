# asking for the customer's first name and storing it in a variable.

first_name = input('hello, what\'s your name?')
surname = input('hello ' + first_name.capitalize() + ', what\'s your surname?')
address = input('what\'s your address, ' + first_name.capitalize() + '?')
phone_number = int(input('what\'s your phone number, ' + first_name.capitalize() + '?'))

print("your first name is " + first_name + ", your surname is " + surname
      + ", your address is " + address + " and your phone no. is " + str(phone_number))
