import sys
input = sys.stdin.read

data = input().split()
n = int(data[0])
straws = list(map(int, data[1:]))

straws.sort(reverse=True)

for i in range(n - 2):
    a, b, c = straws[i], straws[i + 1], straws[i + 2]
    if b + c > a:
        print(a + b + c)
        break
else:
    print(-1)