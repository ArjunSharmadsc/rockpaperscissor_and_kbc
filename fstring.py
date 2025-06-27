name= str("Arjun")
country= str("delhi")
print(f"hi im {name} and i lib=ve in {country}")

#helps in getting a variable in a string

a=(f"{2*30}")
print(a, type(a))

#doctstring:

def square(a):
        ''' this is the docstring and it is given right before the function defination and is not ignored by the interpretor \n and also is used to give a basic understanding of a function'''



square(2)
print(square.__doc__)

#import this    #this is called zen of python

a=int(input("enter a number: "))

for i in range(1,11):
        print(f'{a} x {i} = {a*i}')

