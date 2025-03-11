K = int(input())
size = 1
while size < K:
    size *= 2

if K == size:
    print(size, 0)
else:
    cnt = 0
    temp = size
    remain = K

    while temp > 1 and remain > 0:
        temp //= 2
        cnt += 1
        if remain >= temp:
            remain -= temp

    print(size, cnt)