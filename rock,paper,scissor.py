#rock paper scissor game
import random
comp_choice= random.choice([-1,0,1])
comp=comp_choice


#defining function body and basic logic

def rps():
    x=str(input("enter rock, paper, scissors as r,p,s: "))
    choice_dict={"r": -1,"p":0,"s":1}
    user_num= choice_dict[x]
    print(user_num, type(user_num))
    you=user_num
    try:
        if comp==you:
            print("it is a tie, choose again")
        else:
            if comp== -1 and you == 0:
                print("paper beat rock you won")
            elif comp == 0 and you == 1:
                print("scissor beat paper, you won")
            elif comp == 1 and you == -1:
                print ("rock beat scissor, you won")
            elif comp == 0 and you == -1:
                print("oh, paper beat rock, computer has won")
            elif comp == 1 and you== 0:
                print("oh, scissor beat paper, computer has won")
            elif comp== -1 and you == 1:
                print("oh, rock beats scissor,computer has won")
           
    except ValueError:
        print("look out for the value you have given \n")   

    except KeyError:
        print("only characters r,p,s are allowed \n")
            
    finally:
        print("\n the game is finished, would you like to play again?")
    conti=str(input("say yes or no: "))

    #using recursion here

    if conti=='yes'or conti== 'YES':
        print(rps())
    elif conti== 'no' or conti== 'NO':
        print("good bye")

print(rps())