def prime(a):
    if n>1:
        for i in range(2,a//2+1):
            if a%i==0:
                return(0)
        else:
            return(1)
    else:
        return(0)
def pal(n):
    if n[0]=='-':
        n.pop(0)
    if n==n[::-1]:
        return(1)
    else:
        return(0)
        
n=int(input())
k=1
while(True):
    b=n+k
    if pal(str(b)):
        if prime(b):
            print(b)
            break
    k=k+1