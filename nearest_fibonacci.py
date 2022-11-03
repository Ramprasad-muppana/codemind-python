a=[0,1]
n=int(input())
while(True):
    s=a[-2]+a[-1]
    if s>=n:
        a.append(s)
        break
    else:
        a.append(s)
b=abs(n-a[-1])
c=abs(n-a[-2])
if c==b:
    print(a[-2],a[-1])
elif c<b:
    print(a[-2])
else:
    print(a[-1])