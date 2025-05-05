N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: x[1], reverse=True)

time = float('inf')

for t, s in arr:
    time = min(time, s)
    time -= t
    if time < 0:
        print(-1)
        break
else:
    print(time)