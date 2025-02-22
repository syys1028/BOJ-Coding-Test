import sys
from collections import deque

que = deque()

N = int(sys.stdin.readline().strip())

for i in range(N):
    command = sys.stdin.readline().strip().split()

    if command[0] == 'push':
        que.append(int(command[1]))
    elif command[0] == 'pop':
        print(que.popleft() if que else -1)
    elif command[0] == 'size':
        print(len(que))
    elif command[0] == 'empty':
        print(0 if que else 1)
    elif command[0] == 'front':
        print(que[0] if que else -1)
    elif command[0] == 'back':
        print(que[-1] if que else -1)
