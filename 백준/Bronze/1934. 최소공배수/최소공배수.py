def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

T = int(input())
for i in range(1, T+1):
    a, b = map(int, input().split())
    print(lcm(a, b))