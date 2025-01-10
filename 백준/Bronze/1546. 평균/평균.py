n = int(input())

score = list(map(int, input().split()))
max_score = max(score)
avg = 0
for s in score:
    avg += s / max_score * 100

print(avg/n)