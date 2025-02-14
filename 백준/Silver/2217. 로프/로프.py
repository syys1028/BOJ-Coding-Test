import sys
input = sys.stdin.readline
n = int(input().strip())
ropes = [int(input().strip()) for _ in range(n)]

ropes.sort()

max_weight = 0
for i in range(n):
    max_weight = max(max_weight, ropes[i] * (n - i))

print(max_weight)