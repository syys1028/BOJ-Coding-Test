a, b = map(int, input().split())

result = 0
num = 1
index = 1

while index <= b:
    if index <= b and index + num - 1 >= a:
        result += num * (min(b, index + num - 1) - max(a, index) + 1)
    index += num
    num += 1

print(result)