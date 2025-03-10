S, K = map(int, input().split())

q = S // K
r = S % K

result = 1
for i in range(K):
    if i < r:
        result *= (q + 1)
    else:
        result *= q

print(result)