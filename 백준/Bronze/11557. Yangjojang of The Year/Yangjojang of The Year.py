T = int(input())

for i in range(T):
    arr = {}
    n = int(input())
    while n > 0:
        s, l = input().split()
        arr[s] = int(l)
        n -= 1

    print(max(arr, key=arr.get))