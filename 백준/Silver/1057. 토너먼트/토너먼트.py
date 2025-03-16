N, k, l = map(int, input().split())
num = 0

while k != l:
    k = (k + 1) // 2
    l = (l + 1) // 2
    num += 1

print(num)