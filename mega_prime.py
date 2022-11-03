def prime(a):
    if a>1:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return(0)
        else:
            return(1)
    else:
        return(0)

n=int(input())
if prime(n):
    while(n>0):
        r=n%10
        n=n//10
        if prime(r):
            continue
        else:
            print("Not Mega Prime")
            break
        
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")