import numpy as np

try:
    a= int(input('enter an integer: '))

    print(a, ' is gvien number')
    l1=[1,2]
    print(f'the index of the dic on {a} is: {l1[a]} ')

except ValueError:
    print("invalid value")

except IndexError:
    print("invalid index")



try:
    li=[1,2,4,5,6,7,8]
    i=int(input("enter the value of index"))
    print(li[i])
except:
    print('some error')

#finally clause:

def func():
    try:
        l1=[1,2,3,4,5,6]
        i= int(input('enter an index value to get the dictionary value: '))
        print(l1[i])
        return 1
    except:
        print('invalid value is given')
        return 0
    finally:
        print("this sentence will always be executed regardless of what you give in the code")

x=func()
print(x)

#enumerator:


adic=[2,3,4,5,6,7,10, 11,15]

for index,value in enumerate(adic):
    print(value)
    if (index==4):print("nice")

#now making index from 10
print("enumerated and started from the number 10 \n")

for index,value in enumerate(adic, start=10):
    print(index,value)
    if index==15:
        print("how come")

from kbc import q1,concl1
print(q1)
print(concl1)
