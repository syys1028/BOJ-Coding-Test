T = int(input())
for _ in range(T):
    n = int(input())
    arr = {}

    for _ in range(n):
        name, kind = input().split()
        if kind in arr:
            arr[kind] += 1
        else:
            arr[kind] = 1

    result = 1
    for kind in arr:
        result *= (arr[kind] + 1)

    print(result - 1)
