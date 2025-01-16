n, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

count = 0
for coin in arr:
    if k == 0:
        break
    else:
        count += (k // coin)
        k %= coin

print(count)