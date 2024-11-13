
import random
def dice():
    num=random.randint(1,6)
    return num
print("🚩"*12,"CLIMB FALL","🚩"*12)
a=[]
b=[]
name1=str(input("enter player name1: "))
name2=str(input("enter player name2: "))
i=0
while sum(a)!=10 and sum(b)!=10:
    if(sum(a)<10 and i%2==0):
        print("a's turn : ")
        if(input()=="p"):
            throw=dice()
            a.append(throw)
            print(sum(a))
        i+=1
    elif(sum(b)<10 and i%2!=0):
        print("b's turn : ")
        if(input()=="p"):
            throw=dice()
            b.append(throw)
            print(sum(b))
        i+=1
    elif(sum(a)>10):
        a.clear()
    elif(sum(b)>10):
        b.clear()
    else:
        print("winner")
if(sum(a)==10):
    print(name1," is the winner 😎🔥😎❤️")
else:
    print(name2," is the winner 😎🔥😎❤️")