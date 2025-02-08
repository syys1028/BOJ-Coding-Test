n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

count = 0
arr = set()

for num in numbers:
    target = x - num
    if target in arr:
        count += 1
    arr.add(num)

print(count)
