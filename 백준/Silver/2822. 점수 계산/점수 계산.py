arr = {}

for i in range(1, 9):
    arr[i] = int(input())

arr = sorted(arr.items(), reverse=True, key=lambda x: x[1])

top_5 = arr[:5]
total_score = sum(x[1] for x in top_5)
top_5_keys = sorted(x[0] for x in top_5)

print(total_score)
print(*top_5_keys)