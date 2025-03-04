S = input().strip()

check = 0
arr = []

for ch in S:
    if ch == '(':
        arr.append(ch)
    else:
        if arr:
            arr.pop()
        else:
            check += 1

print(check + len(arr))