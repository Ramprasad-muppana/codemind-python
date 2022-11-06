a,b=map(str,input().split())
b=int(b)
x=a[:b]

y=a[len(a)-b:]

print(abs(int(x)-int(y)))