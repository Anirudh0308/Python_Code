'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([-1,0,1])
youstr = input("Enert your choice (s,w,g): ")
youDict = {"s":1, "w":-1, "g":0}

reverseDict = {1:"snake", -1:"water", 0:"gun"}

you = youDict[youstr]

print(f"you choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")

if(computer == you):
    print("draw")

else:
    if(computer == -1 and you ==1):
        print("you win!")

    elif(computer == -1 and you ==0):
        print("you loos!")

    elif(computer == 1 and you ==0):
        print("you win!")

    elif(computer == 0 and you ==-1):
        print("you win!")

    elif(computer == 0 and you ==1):
        print("you loos!")

    else:
        print("somethink went wrong!")