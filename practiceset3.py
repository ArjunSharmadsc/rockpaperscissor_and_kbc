def great3(x,y,z):
    x=int(input("kindly enter number 1:"))
    y=int(input("\n kindly enter number 2: "))
    z=int(input("\n kindly enter number 3: "))
    try:
        if x>y & x>z:
             print(f' {x} is greater than {y} and {z}')
        elif y>x & y>z:
             print(f' {y} is greater than {z} and {x}')
        elif y==z==x:
             print(f'all number are equal')
        else:
             print(f'{z} is greater than {y} and {x}')
        
    finally:
        print("this sentence will always be executed regardless of what you give in the code")

out=great3(2,3,4)

print(out)

def ap1(n):
   n=int(input("enter a number: \n"))
   if n==1:
       print(n)
   return  sum(n-1)+n

def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))  
    return n 
l=['rohan',' harry', 'aman','kamal',' ankita']

print(rem(l,'an'))
        
        