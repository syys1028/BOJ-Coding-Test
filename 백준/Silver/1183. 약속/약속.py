import sys

data = sys.stdin.read().split()
N = int(data[0])
y = []
index = 1
for i in range(N):
    A = int(data[index])
    B = int(data[index+1])
    index += 2
    y.append(B - A)

y.sort()
if N % 2 == 1:
    print(1)
else:
    m1 = y[N//2 - 1]
    m2 = y[N//2]
    print(m2 - m1 + 1)