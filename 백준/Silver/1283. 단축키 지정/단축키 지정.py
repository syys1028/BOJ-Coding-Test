n = int(input())
options = [input() for _ in range(n)]
used = set()

for line in options:
    words = line.split()
    new_line = line
    found = False

    idx = 0
    for word in words:
        ch = word[0].lower()
        if ch not in used:
            used.add(ch)
            start = new_line.lower().find(word.lower(), idx)
            pos = start + word.lower().find(word[0].lower())
            new_line = new_line[:pos] + "[" + new_line[pos] + "]" + new_line[pos+1:]
            found = True
            break
        idx += len(word) + 1

    if not found:
        for i, ch in enumerate(new_line):
            if ch != ' ' and ch.lower() not in used:
                used.add(ch.lower())
                new_line = new_line[:i] + "[" + new_line[i] + "]" + new_line[i+1:]
                break

    print(new_line)