arr = set()

def d(n):
    return n + sum(int(digit) for digit in str(n))

for number in range(1, 10001):
    arr.add(d(number))

for number in range(1, 10001):
    if number not in arr:
        print(number)