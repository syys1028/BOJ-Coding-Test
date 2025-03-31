cnt = 1

while True:
    s = input()
    if '-' in s:
        break

    stack = []
    ans = 0

    for c in s:
        if c == '{':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                ans += 1
                stack.append('{')

    ans += len(stack) // 2

    print(f"{cnt}. {ans}")
    cnt += 1