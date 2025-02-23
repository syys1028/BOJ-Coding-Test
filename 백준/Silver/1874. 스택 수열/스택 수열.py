import sys

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]

stack = []
arr = []
count = 1
answer = True

for num in numbers:
    while count <= num:
        stack.append(count)
        arr.append("+")
        count += 1

    if stack[-1] == num:
        stack.pop()
        arr.append("-")
    else:
        answer = False
        break

if answer:
    print("\n".join(arr))
else:
    print("NO")