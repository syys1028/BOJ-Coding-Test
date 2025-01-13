import sys
input = sys.stdin.readline

k = int(input().strip())

arr = []
for i in range(k):
    n = int(input().strip())
    if n != 0:
        arr.append(n)
    else:
        arr.pop()

print(sum(arr))