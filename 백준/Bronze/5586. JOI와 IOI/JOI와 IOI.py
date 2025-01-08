arr = input()
joi, ioi = 0, 0
for i in range(len(arr)):
    if arr[i:i+3] == "JOI":
        joi += 1
    elif arr[i:i+3] == "IOI":
        ioi += 1
print(joi)
print(ioi)