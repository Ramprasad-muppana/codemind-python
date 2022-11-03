def prime(a):
    if a>1:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return(0)
        else:
            print(a)
            return(1)
    else:
        return(0)
for _ in range(int(input())):
    a=int(input())
    n=a
    k=1
    b=prime(a)
    while(True):
        if b==1:
            break
        b=prime(a-k)
        if b==1:
            break
        b=prime(a+k)
        k=k+1
        
