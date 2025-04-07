import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    _, start, end = map(int, input().split())
    arr.append((start, end))

arr.sort()
heap = []

for start, end in arr:
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)

print(len(heap))