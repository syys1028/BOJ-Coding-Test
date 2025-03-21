n = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

trees = sorted(zip(A, H))

total = 0
for i in range(n):
    a, h = trees[i]
    total += h + a * i

print(total)