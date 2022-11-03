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
    a=n-k
    b=n+k
    if pal(str(a)):
        print(a,end=' ')
    if pal(str(b)):
        print(b,end=' ')
    if pal(str(a)) or pal(str(b)):
        break
    k=k+1