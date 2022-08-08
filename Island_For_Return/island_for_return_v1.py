# importing random module to get random values

from random import randint

# these two arrays, islands and base_multiplier have the same amount of items, each item in base_multiplier is the multiplier
# for the item in islands with the same index. In island_for_return, the program should ask the user for where their
# location is and multiply the cost of their box based on where they're from.

islands = ['north island', 'south island', 'stewart island']
base_multiplier = [1, 1.5, 2]

height = randint(5, 100)
width = randint(5, 100)
depth = randint(5, 100)

# the reiterative statement should go through all the items in list islands.

answer = input('which island are you from?').strip().lower()

for location in islands:
    if answer == location:
        base_multiplier[islands.index(location)]
