def josephus(n, k):
    arr = list(range(1, n+1))
    result = []
    index = 0
    while arr:
        index = (index + k - 1) % len(arr)
        result.append(arr.pop(index))
    return result

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

result = josephus(n, k)

print("<" + ", ".join(map(str, result)) + ">")