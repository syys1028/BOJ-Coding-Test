n = int(input())

arr = []
for i in range(n):
    data = input().split()
    name = data[0]
    day, month, year = map(int, data[1:])
    arr.append([year, month, day, name])
    
arr.sort()
print(arr[-1][3])
print(arr[0][3])