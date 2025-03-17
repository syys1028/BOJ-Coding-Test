import sys

N = int(sys.stdin.readline().strip())
arr = {}

for _ in range(N):
    filename = sys.stdin.readline().strip()
    a = filename.split(".")[-1]

    if a in arr:
        arr[a] += 1
    else:
        arr[a] = 1

for a in sorted(arr.keys()):
    print(a, arr[a])