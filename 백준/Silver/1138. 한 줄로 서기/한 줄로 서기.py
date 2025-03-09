N = int(input())
arr = list(map(int, input().split()))

result = []

for i in range(N-1, -1, -1):
    left = arr[i]
    result.insert(left, i+1)

print(*result)