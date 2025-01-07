arr = []
T = 0
while T != -1:
    T = int(input())
    arr.append(T)

for i in range(len(arr)-1):
    num = []
    for j in range(1, int(arr[i] ** 0.5) + 1):
        if arr[i] % j == 0:
            num.append(j)
            if j != 1 and j != arr[i] // j:
                num.append(arr[i] // j)
    num.sort()
    if arr[i] == sum(num):
        print(f"{arr[i]} = {' + '.join(map(str, num))}")
    else:
        print(f"{arr[i]} is NOT perfect.")