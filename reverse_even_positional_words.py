s=list(map(str,input().split()))
for i in range(0,len(s)):
    a=s[i]
    if i%2==0:
        print(a[::-1],end=" ")
    else:
        print(a,end=" ")