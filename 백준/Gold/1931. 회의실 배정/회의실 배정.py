import sys
input = sys.stdin.read

data = input().splitlines()
n = int(data[0])
arr = [tuple(map(int, line.split())) for line in data[1:]]

arr.sort(key=lambda x: (x[1], x[0]))

count = 0
current_time = 0

for start, end in arr:
    if start >= current_time:
        count += 1
        current_time = end

print(count)