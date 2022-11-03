s=list(map(str,input().split()))
a=[]
for i in s:
    i=i[::-1]
    a.insert(0,i)
print(' '.join(a))