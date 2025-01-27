import math

n, m = map(int, input().split())
num = math.gcd(n, m)
print("1" * num)