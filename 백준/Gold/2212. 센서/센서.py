n = int(input())
k = int(input())
arr = list(map(int, input().split()))

if k >= n:
    print(0)

else:
    arr.sort()
    num = [arr[i+1] - arr[i] for i in range(n - 1)]
    num.sort(reverse=True)
    for _ in range(k - 1):
        num.pop(0)
    print(sum(num))