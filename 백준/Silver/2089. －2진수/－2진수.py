n = int(input())
if n == 0:
    print(0)
else:
    result = ""
    while n != 0:
        n, num = divmod(n, -2)
        if num < 0:
            n += 1
            num += 2
        result = str(num) + result
    print(result)