x = int(input())

for i in range(x):
    gap = 0
    arr = list(map(int, input().split()))
    num = arr.pop(0)

    arr.sort(reverse=True)
    for j in range(len(arr)-1):
        if arr[j] - arr[j+1] > gap:
            gap = arr[j] - arr[j+1]

    print(f"Class {i+1}")
    print(f"Max {max(arr)}, Min {min(arr)}, Largest gap {gap}")