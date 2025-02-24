import sys

N, M = map(int, sys.stdin.readline().split())

arr1 = set(sys.stdin.readline().strip() for _ in range(N))
arr2 = sorted(name.strip() for name in sys.stdin if name.strip() in arr1)

arr2.sort()
print(len(arr2))
print("\n".join(arr2))