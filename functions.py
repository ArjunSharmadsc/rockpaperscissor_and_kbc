#basic function declaration
def meanof2(x,y):
    a=(x*y)/(x+y)
    print(a)

meanof2(2,4)
print("another example \n")

meanof2(34,56) 
print("\n")

#function with nested if and loops:

x=int(input("enter 1 number: "))
y= int(input ("enter another number: "))
print("number 1 is ", x, "\n")
print("number 2 is ", y, "\n")

def greater(a,b):
    if a>b:
        print (a , " is greater")
    elif a==b:
        print("both are equal")
    else:
        print(b, " is greater")

greater(x,y)

#default arguement function:

print(("default arguement function"))
def a(a=1,b=3):
    print(" sum of default numbers: ", a+b)
a()

#keyword function:
def avg(a=2, b=4):
    print("avg of 2 numbers is: ", (a+b)/2)

avg(b=3, a=4) #the order of the value is not important

#required arguement function:
def req(a):
    print(a)
req(int(input("give a value for a required arguement function: ")))

#variable arguement function:
#1. arbitrary funtion: make the variable in tuple:

def aver(*number):
    print(type(number))
    for i in number:
        sum=i+i
        print ("the average is: ", sum/len(number))

aver(1,2,3,4)

#recursion

def factorial(n): 
    
    if (n==1 or n==0): 
        return 1
    else: 
        return (n * factorial(n - 1)) 
num = 5; 
print("number : ",num)
print("Factorial : ",factorial(num))
      

