temp = ""
arr = ""
while temp != "END":
    temp = input()
    if temp == "END":
        break
    else:
        temp = list(temp)
        temp.reverse()
        temp = ''.join(temp)
        arr += temp
        arr += "\n"

print(arr)