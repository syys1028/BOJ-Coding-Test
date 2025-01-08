T = int(input())

for i in range(T):
    n = list(input())
    if n[len(n)//2-1] == n[len(n)//2]:
        print("Do-it")
    else:
        print("Do-it-Not")