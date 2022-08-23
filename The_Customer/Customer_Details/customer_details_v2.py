# asking for the customer's first name and storing it in a variable.

first_name = input('hello, what\'s your name?').strip().lower()
surname = input('hello ' + first_name.title() + ', what\'s your surname?').strip().lower()
address = input('what\'s your address, ' + first_name.title() + '?').strip().lower()
phone_number = int(input('what\'s your phone number, ' + first_name.title() + '?'))
