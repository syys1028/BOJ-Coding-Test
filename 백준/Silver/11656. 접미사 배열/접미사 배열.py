import sys

S = sys.stdin.readline().strip()

arr = []
for i in range(len(S)):
    arr.append(S[i:])

arr.sort()

for a in arr:
    print(a)