s=input()
a='aeiou'
f=0
for i in a:
    if i not in s:
        print(i,end=' ')
        f=1
if f==0:
    print(0)