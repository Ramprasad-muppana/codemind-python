def prime(a):
    if a>1:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return(0)
        else:
            return(1)
    else:
        return(0)
        
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    c=c+prime(i)
print(c)    