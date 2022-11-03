s=input()
a='aeiou'
A='AEIOU'
a1=0
A1=0
for i in a:
    if i in s:
        a1=a1+1
for i in A:
    if i in s:
        A1=A1+1
if a1==5 or A1==5:
    print("True")
else:
    print("False")
    
    
    