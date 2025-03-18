import sys
M, N = map(int, sys.stdin.readline().split())
numbers = []
num_to_str = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for num in range(M, N + 1):
    english = " ".join(num_to_str[int(digit)] for digit in str(num))
    numbers.append((english, num))
numbers.sort()
for i in range(len(numbers)):
    print(numbers[i][1], end=" ")
    if (i + 1) % 10 == 0:
        print()