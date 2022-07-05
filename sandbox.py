base_multi = {'north island': 1, 'south island': 1.5, 'stewart island': 2}

money = 8
answer = input('enter input')
for i in base_multi.keys():
    if i == answer:
        money *= base_multi[i]

base_multi.update( )
