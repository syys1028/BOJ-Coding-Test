n = int(input())
a = 2

while a <= (n // 2 + 1):
    if n % a == 0:
        n = n // a
        print(a)
    else:
        a += 1
    if a > (n // 2 + 1) and n != 1:
        print(n)
