def get_hcf(a, b):
    while b:
        a, b = b, a%b
    return a

def get_lcm(a, b):
    return a*b//get_hcf(a,b)

test_case = int(input())
for _ in range(test_case):
    n, a, b, k = map(int, input().split())
    var = get_lcm(a, b)
    new = n//a + n//b - 2*(n//var)
    if new>=k:
        print('Win')
    else:
        print('Lose')