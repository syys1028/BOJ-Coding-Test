n, l = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

for num in arr:
    if l >= num:
        l += 1
    else:
        break
print(l)