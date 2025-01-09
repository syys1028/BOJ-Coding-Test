a, b = map(int,input().split())

gcd, icm = 0, 0
for i in range(1, a if a>b else b+1):
    if a % i == 0 and b % i == 0:
        gcd = i

icm = gcd * (a // gcd) * (b // gcd)

print(gcd)
print(icm)