import sys
from collections import Counter

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
cards = list(map(int, data[1].split()))

M = int(data[2])
targets = list(map(int, data[3].split()))

card_count = Counter(cards)

print(" ".join(str(card_count[num]) for num in targets))