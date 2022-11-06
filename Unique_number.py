n=input()
b=list(n)
for i in b:
    c=n.count(i)
    if c!=1:
        print("Not Unique Number")
        break
else:
    print("Unique Number")