x=str(input("enter rock, paper, scissors as r,p,s: "))
choice_dict={"r": -1,"p":0,"s":1}
user_num= choice_dict[x]
print(user_num, type(user_num))