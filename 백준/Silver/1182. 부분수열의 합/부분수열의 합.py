import sys

def dfs(index, n_sum):
    global count
    if index >= N:
        return
    
    n_sum += sequence[index]
    
    if n_sum == S:
        count += 1

    dfs(index + 1, n_sum)
    dfs(index + 1, n_sum - sequence[index])

N, S = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))

count = 0
dfs(0, 0)

print(count)