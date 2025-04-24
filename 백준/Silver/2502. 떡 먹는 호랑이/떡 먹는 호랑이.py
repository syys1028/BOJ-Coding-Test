D, K = map(int, input().split())

for A in range(1, K + 1):
    for B in range(A, K + 1):
        arr = [0] * D
        arr[0] = A
        arr[1] = B
        for i in range(2, D):
            arr[i] = arr[i - 2] + arr[i - 1]
        if arr[D - 1] == K:
            print(A)
            print(B)
            exit()
