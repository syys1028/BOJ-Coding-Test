import sys
input = sys.stdin.readline

N = int(input().strip())
road_lengths = list(map(int, input().split()))
price = list(map(int, input().split()))

min_cost = 0
min_price = price[0]

for i in range(N - 1):
    min_cost += min_price * road_lengths[i]
    if price[i + 1] < min_price:
        min_price = price[i + 1]

print(min_cost)