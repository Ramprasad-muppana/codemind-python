
n=int(input())
b=[2,3,5]
if n==1:
    print("Ugly Number")
else:
    a=[]
    while(n%2==0):
        n=n//2
        a.append(2)

    if n!=1:
        while(n%3==0):
            n=n//3
            a.append(3)
       
    if n!=1:
        while(n%5==0):
            n=n//5
            a.append(5)
        
    if n!=1:
        a.append(n)
    for i in a:
        if i not in b:
            print("Not Ugly Number")
            break
    else:
        print("Ugly Number")
