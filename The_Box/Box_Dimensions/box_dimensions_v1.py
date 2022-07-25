# program running, if it goes as expected the program should work for integer inputs and crash for float or string
# inputs or empty string inputs. The program also shouldn't reiterate itself asking the user for input or display an
# error message (since the inputs here wouldn't). Also the information such as the dimensions of the boxes are stored
# in their individual variables.

height = int(input('enter height'))

width = int(input('enter width'))

depth = int(input('enter depth'))

print('this is {} cm tall, {} cm wide and {} cm thick'.format(height, width, depth))
