import sys
import math
n = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]

gaps = [arr[i] - arr[i-1] for i in range(1, n)]

gcd_val = gaps[0]
for i in range(1, len(gaps)):
    gcd_val = math.gcd(gcd_val, gaps[i])

result = sum((gap // gcd_val - 1) for gap in gaps)

print(result)