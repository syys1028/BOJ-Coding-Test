T = int(input())
for _ in range(T):
    N = int(input())
    li = list(map(int, input().split()))
    li.sort()

    arr = [0] * N
    left, right = 0, N - 1
    for i in range(N):
        if i % 2 == 0:
            arr[left] = li[i]
            left += 1
        else:
            arr[right] = li[i]
            right -= 1

    num = 0
    for i in range(N):
        d = abs(arr[i] - arr[(i + 1) % N])
        num = max(num, d)

    print(num)