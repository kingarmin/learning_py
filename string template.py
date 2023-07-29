# A Simple Python template example
from string import Template
# Create a template that has placeholder for value of x
t = Template('x is $x')
# Substitute value of x in above template
print("EXP1: ")
print (t.substitute({'x' : 1}))



print("EXP2: ")
data={('armin',18) , ('parsa',17) , ('yekta',16)}
for i in data:
    print(Template('$name is $age').substitute(name=i[0],age=i[1]))