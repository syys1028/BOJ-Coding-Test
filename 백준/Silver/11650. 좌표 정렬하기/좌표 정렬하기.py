import sys

n = int(sys.stdin.readline().strip())
points = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    points.append((x, y))

points.sort()

for x, y in points:
    print(x, y)