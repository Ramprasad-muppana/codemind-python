n=int(input())
a=n
k=0
while(n!=0):
    n=n//2
    if n==0:
        break
    k=k+1
n=(2**k)
n1=(2**(k+1))
n=abs(a-n)
n1=abs(a-n1)
print(min(n,n1))