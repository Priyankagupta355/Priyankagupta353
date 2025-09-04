import random
computer = random.choice([-1,0,1])
youstr=input("Enter Your Choice :")
youDict = {"s":1,"w":-1,"g":0}
reverseDict= {1:"Snake",-1:"Water",0:"Gun"}

you = youDict[youstr]

print(f"You Choice{reverseDict[you]}\nComputer Choice {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")

else:
    if(computer == -1 and you ==1):
        print("You win!")    

    elif(computer ==-1 and you ==0):
        print("You Lose!")    
    elif(computer == 1 and you == -1):
        print("You Lose!")    
    elif(computer == 0 and you == -1):
        print("You win!")    
    elif(computer == 1 and you == 0):
        print("you win!")   

    else:
        print("Oops !,Something went Wrong...")     