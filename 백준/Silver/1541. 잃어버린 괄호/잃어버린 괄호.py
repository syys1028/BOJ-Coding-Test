def min_div(n):
    parts = n.split('-')
    result = sum(map(int, parts[0].split('+')))
    for part in parts[1:]:
        result -= sum(map(int, part.split('+')))
    return result

n = input().strip()
print(min_div(n))