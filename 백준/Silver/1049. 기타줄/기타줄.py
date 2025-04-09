N, M = map(int, input().split())
p_min = 1001
s_min = 1001

for _ in range(M):
    p, s = map(int, input().split())
    p_min = min(p_min, p)
    s_min = min(s_min, s)

cost1 = s_min * N
cost2 = ((N + 5) // 6) * p_min
cost3 = (N // 6) * p_min + (N % 6) * s_min

print(min(cost1, cost2, cost3))