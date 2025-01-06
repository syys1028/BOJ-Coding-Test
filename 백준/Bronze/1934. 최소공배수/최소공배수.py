def max_num(a, b):
    num = 1
    if a > b:
        m = b
    else:
        m = a
    for i in range(2, m+1):
        if a % i == 0 and b % i == 0:
            num = i
    return num

T = int(input())
for i in range(1, T+1):
    a, b = input().split()
    a, b = int(a), int(b)
    num = max_num(a, b)
    print((a // num) * (b // num) * num)