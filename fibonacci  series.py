#fibanocii series
#0 1 1 2 3 5 8 13 . . . . .
# write a program to print the first n numbers in the fibanocii series
n=int(input("enter the values"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    