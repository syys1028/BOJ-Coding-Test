N, L = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
count = 0
check = 0

while check < N:
    count += 1
    start = arr[check]
    lens = start + L - 1

    check += 1
    while check < N and arr[check] <= lens:
        check += 1

print(count)