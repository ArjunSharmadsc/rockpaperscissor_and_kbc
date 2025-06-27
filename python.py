import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# plt.plot(x, y)

# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Simple Plot')

# plt.show()

# print("hi", 7, 5.5, sep="&")
# print ("the type of y is", type(y))
a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
print("number1 is \n", a, "\n the number2 is \n", b)
c=input("give the operand")
if c == "+": print(a+b)
elif c =="-" : print(a-b)
elif c=="*" : print(a*b)
elif c=="/" : print(a/b)
elif c=="%" : print(a%b)
else: print("give the valid operand")
# print(int(3.99))
# print(1+3*2)
# STR1 = "hi im Arjun sharma, been a while folks"
# print(STR1.endswith("lks")) 
# print(STR1.find("Ar"))

num1=int(input("enter your age: \n"))
if num1 >= 18 & num1 < 45 :
    if num1 == 18:
        print("you are just at the nick of time")

    else:
        print ("you are an eligible adult")
elif num1 >= 45 & num1 < 60 :
    print ("alright old man")
else:
    print("boy you are old, just retire\n")

