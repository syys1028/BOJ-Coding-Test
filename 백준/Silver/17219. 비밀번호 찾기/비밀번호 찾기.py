import sys
N, M = map(int, sys.stdin.readline().split())
arr = {}

for i in range(N):
    text1, text2 = map(str, sys.stdin.readline().split())
    arr[text1] = text2

for i in range(M):
    texts = str(sys.stdin.readline().strip())
    print(arr[texts])