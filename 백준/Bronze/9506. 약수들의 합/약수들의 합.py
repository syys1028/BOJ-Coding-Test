arr = []
T = 0
while T != -1:
    T = int(input())
    arr.append(T)

for i in range(len(arr)-1):
    num = []
    for j in range(1, arr[i]//2+1):
        if arr[i] % j == 0:
            num.append(j)
    if arr[i] == sum(num):
        print("{} = ".format(arr[i]), end="")
        for n in range(len(num)-1):
            print("{} + ".format(num[n]), end="")
        print("{}".format(num[len(num)-1]))
    else:
        print("{} is NOT perfect.".format(arr[i]))