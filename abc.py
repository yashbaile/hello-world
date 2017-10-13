l=[]
c=0
while c < 10:
    n=int(input("Enter"))
    l.append(n)
    c=c+1
    for i in l:
        if i%2==0:
            print("Num is even")
        else i%2!=0:
            print("Num is odd")
        break
