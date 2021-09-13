list = [x for x in range(1,47) if x % 3 == 0]
print(list)

print('Drugi list comprehension')
dict2 = {'Jacek': 400, 'Grzepcio': 700}
list2 = ['kuba' for x in dict2.keys()]

print(list2)

print('----------')

def funkcyjka(a):
    return (a+5) / 2

list3 = [funkcyjka(y) for y in range(12)]
print(list3)

print('-------')

list4 =[[j for j in range(4)] for i in range(4)]
print(list4)

print('----')
list5 = [k
    for l in range(4)
    for k in range(4)]
print(list5)
