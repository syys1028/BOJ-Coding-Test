t = int(input());

for i in range(1, t+1):
    a, b = input().split();
    sum = int(a) + int(b)
    print("Case #{}: {} + {} = {}".format(i,a,b,sum));