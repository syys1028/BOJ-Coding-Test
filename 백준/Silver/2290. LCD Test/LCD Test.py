def lcd_display(s, n):
    digits = {
        0: [0, 1, 2, 3, 4, 5],
        1: [1, 2],
        2: [0, 1, 6, 4, 3],
        3: [0, 1, 6, 2, 3],
        4: [5, 6, 1, 2],
        5: [0, 5, 6, 2, 3],
        6: [0, 5, 6, 4, 3, 2],
        7: [0, 1, 2],
        8: [0, 1, 2, 3, 4, 5, 6],
        9: [0, 1, 2, 3, 5, 6],
    }

    def build_line(line_type):
        line = []
        for ch in str(n):
            d = int(ch)
            seg = digits[d]
            if line_type == 0:
                line.append(" " + ("-" * s if 0 in seg else " " * s) + " ")
            elif 1 <= line_type <= s:
                left = "|" if 5 in seg else " "
                right = "|" if 1 in seg else " "
                line.append(left + " " * s + right)
            elif line_type == s + 1:
                line.append(" " + ("-" * s if 6 in seg else " " * s) + " ")
            elif s + 2 <= line_type <= 2 * s + 1:
                left = "|" if 4 in seg else " "
                right = "|" if 2 in seg else " "
                line.append(left + " " * s + right)
            elif line_type == 2 * s + 2:
                line.append(" " + ("-" * s if 3 in seg else " " * s) + " ")
        return " ".join(line)

    for i in range(2 * s + 3):
        print(build_line(i))

s, n = map(int, input().split())
lcd_display(s, n)