import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    arr.sort()

    count = 1 
    rank = arr[0][1]

    for i in range(1, N):
        if arr[i][1] < rank:
            count += 1
            rank = arr[i][1]

    print(count)