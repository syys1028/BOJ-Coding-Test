D, K = map(int, input().split())

arr = [(1, 0), (0, 1)]

for i in range(2, D):
    a1, b1 = arr[i - 1]
    a2, b2 = arr[i - 2]
    arr.append((a1 + a2, b1 + b2))

a, b = arr[D - 1]
 
for A in range(1, K + 1):
    if (K - a * A) % b == 0:
        B = (K - a * A) // b
        if A <= B:
            print(A)
            print(B)
            break