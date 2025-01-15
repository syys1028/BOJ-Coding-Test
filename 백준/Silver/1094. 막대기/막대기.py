x = int(input())

first = [64]
while sum(first) != x:
    a = first.pop(first.index(min(first)))
    first.append(a // 2)
    if sum(first) < x:
        first.append(a // 2)
        
print(len(first))