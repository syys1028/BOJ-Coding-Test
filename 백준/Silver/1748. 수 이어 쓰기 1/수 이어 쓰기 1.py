def check_n(N):
    length = 0
    num = 1
    start = 1
    
    while start * 10 <= N:
        count = start * 9
        length += count * num
        start *= 10
        num += 1

    length += (N - start + 1) * num
    return length

N = int(input())
print(check_n(N))