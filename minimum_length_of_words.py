s=list(map(str,input().split()))
a=[]
for i in s:
    a.append(len(i))
print(min(a))