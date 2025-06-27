import matplotlib as plt
import pandas as pd
import numpy as np
ls=[1,2,3,4]
print(ls[3])
l1=[i*i for i in range(4)]
print(l1)
l2=[i*i for i in range(10 ) if i%2==0]
print(l2)

#sets:
s1={1,2,3,4}
print("the set used here is ", s1, " and the type is :", type(s1))
for values in s1:
    print(values)

strconverted=[input("enter set2: ")]
s2=set(strconverted)
print("set 1 is : ", s1, " and set2 is: ", s2, "\n and there union is:")
print(s1.union(s2))

print("simiarily here is the intersection:")
print(s1.intersection(s2))

#updating a set:
s1.update(s2)
print("updated set1: ", s1)
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
z=[20,30,45,66,73]
A1=[21,44,54,77,85]
j=[43,66,73,12,21]
plt.plot(z,j)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')

plt.show() 

dict={'name':'arjun', 'age': 20, 'eligible':'yes'}
print(dict)
print("they key of dict are", dict.keys()) 

for keys in dict.keys():
    print(dict[keys])
    print(f'the value corresponding to {keys} is: {dict[keys]}')