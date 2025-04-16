ac=int(input("enter actual amount"))
sc=int(input("enter sales amount"))

if sc>ac:
    print("profit: $",sc-ac)

else:
    print("loss: $",ac-sc)