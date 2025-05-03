word = input()

croatia = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]

for c in croatia:
    word = word.replace(c, "X")
    
print(len(word))