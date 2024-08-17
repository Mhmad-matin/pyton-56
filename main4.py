mylist=[]
x=int(input("Please enter the number of members on your list?"))
for i in range(x):
    y=int(input("enetr your number:"))
    mylist.append(y)
for I in range(len(mylist)):
    for g in range(I+1 , len(mylist)):
        if mylist[I]<mylist[g]:
            mylist[g], mylist[I] = mylist[I], mylist[g]
print(mylist)                
