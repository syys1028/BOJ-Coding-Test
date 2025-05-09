n, d = input().split()
n = int(n)

count = ''.join(str(i) for i in range(1, n + 1)).count(d)

print(count)