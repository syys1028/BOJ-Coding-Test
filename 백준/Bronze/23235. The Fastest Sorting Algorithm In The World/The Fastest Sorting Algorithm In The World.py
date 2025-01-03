temp = 1
count = 0
while (temp != 0):
    arr = list(map(int, input().split()))
    temp = arr[0]
    if temp == 0:
        break
    else:
        count += 1
        for i in range(temp-1):
            arr[i] = arr[i+1]
        sorted(arr)

for i in range(1,count+1):
    print("Case {}: Sorting... done!".format(i))