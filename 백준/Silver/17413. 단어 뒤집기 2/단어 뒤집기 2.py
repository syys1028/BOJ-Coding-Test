import sys

def re_word(S):
    result = []
    word = []
    in_tag = False

    for char in S:
        if char == '<':
            if word:
                result.append(''.join(word[::-1]))
                word.clear()
            in_tag = True
            result.append(char)
        elif char == '>':
            in_tag = False
            result.append(char)
        elif in_tag:
            result.append(char)
        else:
            if char == ' ':
                result.append(''.join(word[::-1]))
                result.append(' ')
                word.clear()
            else:
                word.append(char)

    if word:
        result.append(''.join(word[::-1]))

    return ''.join(result)

S = sys.stdin.readline().strip()
print(re_word(S))