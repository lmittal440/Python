p1=str(input("player 1 enter your choice"))
p2=str(input("player 2 enter your choice"))

if(p1=="stone" or p1=="paper" or p1=="scissor" and p2=="stone" or p2=="paper" or p2=="scissor"):
    if(p1=="stone"):
        if(p2=="paper"):
            flag=True
        else:
            flag=False

    if(p1=="paper"):
        if(p2=="scissor"):
            flag=False
        else:
            flag=True

    if(p1=="scissor"):
        if(p2==stone):
            flag=False
        else:
            flag=True

else:
    print("Invalid input")

if(flag):
    print("player 1 wins")
else:
    print("player 2 wins")
