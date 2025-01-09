n = int(input())

arr = {}
for i in range(n):
    lists = list(map(str, input().split()))
    if int(lists[1]) < 10:
        lists[1] = "0" + lists[1]
    elif int(lists[2]) < 10:
        lists[2] = "0" + lists[2]

    arr[lists[0]] = lists[3]+lists[2]+lists[1]

print(max(arr, key=arr.get))
print(min(arr, key=arr.get))