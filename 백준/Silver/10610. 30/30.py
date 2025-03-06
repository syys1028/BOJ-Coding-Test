N = input().strip()
digits = list(N)

if '0' not in digits:
    print(-1)
else:
    if sum(map(int, digits)) % 3 != 0:
        print(-1)
    else:
        digits.sort(reverse=True)
        print(''.join(digits))
