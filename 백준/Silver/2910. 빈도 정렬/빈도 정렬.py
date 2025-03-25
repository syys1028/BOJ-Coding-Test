import sys
from collections import Counter

N, C = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))

order = {}
for idx, num in enumerate(sequence):
    if num not in order:
        order[num] = idx

count = Counter(sequence)

sorted_seq = sorted(sequence, key=lambda x: (-count[x], order[x]))

print(*sorted_seq)