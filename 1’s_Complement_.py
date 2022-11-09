def bswitch(num):
    c = 1
    while num*2 > c:
        num = num ^ c
        c = c << 1
    return num
n=int(input())
print(bswitch(n))