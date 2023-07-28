data= {
    101:{'name' : 'ARMIN' , 'age' : 17},
    102:{'name' : 'Yekta' , 'age' : 16},
}
item1=data[101]
item2=data[102]
print('methode 1')
print(item1['name'],'is',item1['age'])

print('methode 2')
t=(item1['name'],'is',str(item1['age']))
s='_'.join(t)
print(s)

print('methode 3')
s='%s is %s' %(item2['name'],item2['age'])
print(s)

print('methode 4')
s='{} is {}'.format(item1['name'],item1['age'])
print(s)

print('method 5')
print(f'{item1["name"]} is {item1["age"]}')
print(f'{item2["name"]} is {item2["age"]}')