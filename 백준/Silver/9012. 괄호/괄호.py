T = int(input())

for i in range(T):
    arr = list(input())
    check = []
    answer = True

    for j in range(len(arr)):
        if arr[j] == '(':
            check.append(arr[j])
        else:
            if check:
                check.pop()
            else:
                answer = False
                break
                
    if answer and len(check) == 0:
        print("YES")
    else:
        print("NO")