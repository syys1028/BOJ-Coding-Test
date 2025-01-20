import sys

data = sys.stdin.read().split()

n = int(data[0])
arr_n = set(map(int, data[1:n+1]))

m = int(data[n+1])
arr_m = map(int, data[n+2:n+2+m])

print(" ".join("1" if num in arr_n else "0" for num in arr_m))