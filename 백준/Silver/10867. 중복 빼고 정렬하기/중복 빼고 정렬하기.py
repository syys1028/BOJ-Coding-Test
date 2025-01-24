import sys

n = int(sys.stdin.readline().strip())

arr = set(map(int, sys.stdin.readline().split()))

sorted_arr = sorted(arr)
print(' '.join(map(str, sorted_arr)))