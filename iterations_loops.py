dict1 = {'Kacha': 1, 'Bacha': 2, 'Lacha': 3, 'Czacha': 4}

for v in dict1.values():
    print('Drukuje wartosci: ', v)

print('-------------')

for key in dict1:
    print('Teraz keys: ', key)

print('Albo tak, ale to mniej eleganckie:')

for key in dict1.keys():
    print(key)