s = input().strip()
arr = set()

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        arr.add(s[i:j])

print(len(arr))