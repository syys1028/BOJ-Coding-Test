import sys

N = int(sys.stdin.readline().strip())
num = [sys.stdin.readline().strip() for _ in range(N)]

num.sort(key=lambda x: (len(x), sum(int(c) for c in x if c.isdigit()), x))

print("\n".join(num))