import sys

N = int(sys.stdin.readline().strip())
arr = []

for i in range(N):
    age, name = sys.stdin.readline().split()
    arr.append((int(age), i, name))

arr.sort(key=lambda x: (x[0], x[1]))

for age, _, name in arr:
    print(age, name)