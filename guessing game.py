import random

radndomNum = random.randint(1, 100)

print("you can exit the game any time by inserting zero (0)")
userNum = int(input("please guess the Number  :"))
while radndomNum != userNum:
    if userNum == 0:
        break
    elif radndomNum > userNum:
        print("the number is higher !")
    elif radndomNum < userNum:
        print("the number is lower !")
    userNum = int(input("please guess the Number  :"))

if userNum == 0:
    print("Game ended !!!")
else:
    print("the number is correct :", userNum)
