N = int(input())
arr = [input().strip() for _ in range(N)]
l = len(arr[0])

for k in range(1, l + 1):
    s = set()
    for num in arr:
        s.add(num[-k:])
    if len(s) == N:
        print(k)
        break