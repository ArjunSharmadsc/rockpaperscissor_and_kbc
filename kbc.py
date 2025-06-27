print("welcome to kbc, kindly enter your name: ")
name=str(input())
print(name)
print("hello", name, "lets play kbc\n")
print("pehla prashan apki screen par yeh raha \n")
print("how many hearts does an octopus have?")
q1={'a':3,'b':4, 'c':2, 'd':7}
print(q1)
print("type your answer here: ")
ansq1=str(input())
def concl1(ansq1):
    if ansq1 == 'a'in q1:
        print("cangratulations you have won $100")
    if ansq1 != 'a':
        print("apsos yeh galat jwab h")
    return ansq1
    
c=concl1(ansq1)
if c== True:
    print("apki kul rashi ho chuki h $100")

if c == False:
    print("aap kuch bhi nahi jeete")

print("chaliye badhte h doosre sawal ki or \n")

