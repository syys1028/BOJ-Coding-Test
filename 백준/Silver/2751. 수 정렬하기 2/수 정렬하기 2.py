import sys

n = int(sys.stdin.readline().strip())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()
sys.stdout.write('\n'.join(map(str, arr)) + '\n')
