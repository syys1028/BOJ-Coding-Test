N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

while True:
    if arr[r][c] == 0:
        arr[r][c] = -1
        count += 1

    cleaned = False
    for _ in range(4):
        d = (d + 3) % 4
        nx, ny = r + dx[d], c + dy[d]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
            r, c = nx, ny
            cleaned = True
            break

    if not cleaned:
        back = (d + 2) % 4
        bx, by = r + dx[back], c + dy[back]
        if 0 <= bx < N and 0 <= by < M and arr[bx][by] != 1:
            r, c = bx, by
        else:
            break

print(count)