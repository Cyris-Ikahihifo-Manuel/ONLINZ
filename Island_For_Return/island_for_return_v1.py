# importing random module to get random values

import random

# these two arrays, islands and base_multiplier each store the same amount of information. In island_for_return, the
# program should ask the user for where their location is and multiply the cost of their box based on where they're from.

islands = ['north island', 'south island', 'stewart island']
base_multiplier = [1, 1.5, 2]

height = random.randint(5, 100)
width = random.randint(5, 100)
depth = random.randint(5, 100)

# this should go through the array of islands. If it goes as expected the program shouldn't reiterate itself

answer = input('which island are you from?').strip().lower()

for location in islands:
    if answer == location:
        base_multiplier[islands.index(location)]
