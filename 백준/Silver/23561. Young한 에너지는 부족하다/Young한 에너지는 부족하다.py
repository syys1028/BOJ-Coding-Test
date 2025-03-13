import sys
input = sys.stdin.readline
N = int(input())
ages = list(map(int, input().split()))

ages.sort()

m = [ages[i + N] for i in range(N)]

result = max(m) - min(m)
print(result)