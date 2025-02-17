import sys

def check_num(m, n):
    is_prime = [True] * (n + 1)  
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:  
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    for num in range(m, n + 1):
        if is_prime[num]:
            print(num)

m, n = map(int, sys.stdin.readline().split())
check_num(m, n)