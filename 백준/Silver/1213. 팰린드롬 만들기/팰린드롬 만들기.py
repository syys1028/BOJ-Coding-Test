from collections import Counter

name = input()
counter = Counter(sorted(name))

mid = ''
half = ''

odd_count = 0
for char in counter:
    cnt = counter[char]
    if cnt % 2 == 1:
        odd_count += 1
        mid = char
    half += char * (cnt // 2)

if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    print(half + mid + half[::-1])