s = list(input())
t = list(input())

while len(t) > len(s):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()

print(1 if t == s else 0)