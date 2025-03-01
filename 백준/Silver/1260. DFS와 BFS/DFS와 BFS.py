import sys
from collections import deque
sys.setrecursionlimit(10**6)

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

visited = [False] * (n + 1)
dfs_result = []

def dfs(node):
    visited[node] = True
    dfs_result.append(node)
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

dfs(v)

bfs_result = []
visited_bfs = [False] * (n + 1)
queue = deque([v])
visited_bfs[v] = True

while queue:
    node = queue.popleft()
    bfs_result.append(node)
    for next_node in graph[node]:
        if not visited_bfs[next_node]:
            visited_bfs[next_node] = True
            queue.append(next_node)

print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))