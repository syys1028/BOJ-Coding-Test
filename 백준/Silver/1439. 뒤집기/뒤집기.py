s = input().strip()

count0 = 0
count1 = 0

if s[0] == '0':
    count0 += 1
else:
    count1 += 1

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        if s[i] == '0':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))