n = int(input())
votes = [int(input()) for _ in range(n)]

d = votes[0]
others = votes[1:]
count = 0

if n == 1:
    print(0)
else:
    while True:
        if not others:
            break
        max_vote = max(others)
        if d > max_vote:
            break
        max_index = others.index(max_vote)
        others[max_index] -= 1
        d += 1
        count += 1
    print(count)