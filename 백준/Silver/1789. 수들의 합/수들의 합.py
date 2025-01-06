s = int(input())
max_num = 0
n = s
while n > -1:
    if (n - (max_num + 1)) >= 0:
        max_num += 1
        n = n - max_num
    else:
        print(max_num)
        n = -1