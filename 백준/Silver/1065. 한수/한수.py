def check_num(num):
    arr = list(map(int, str(num)))
    if len(arr) <= 2:
        return True
    diff = arr[1] - arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i + 1] - arr[i] != diff:
            return False
    return True

N = int(input())
count = 0
for i in range(1, N + 1):
    if check_num(i):
        count += 1
print(count)