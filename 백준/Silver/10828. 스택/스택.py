import sys
stack = []

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        a = -1
    else:
        a = stack.pop()
    print(a)

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])


n = int(sys.stdin.readline().strip())
for i in range(n):
    texts = sys.stdin.readline().split()
    if texts[0] == "push":
        push(int(texts[1]))
    elif texts[0] == "pop":
        pop()
    elif texts[0] == "size":
        size()
    elif texts[0] == "empty":
        empty()
    elif texts[0] == "top":
        top()
