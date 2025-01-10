n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    f1, f2, fn = 0, 1, 0
    while n > 1:
        fn = f1 + f2
        f1, f2 = f2, fn
        n -= 1
    print(fn)