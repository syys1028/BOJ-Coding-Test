import sys
input = sys.stdin.read
data = input().splitlines()

def check_s(s, t):
    s_idx = 0
    for char in t:
        if s_idx < len(s) and s[s_idx] == char:
            s_idx += 1
        if s_idx == len(s):
            return "Yes"
    return "No"

for line in data:
    if line.strip():
        s, t = line.split()
        print(check_s(s, t))