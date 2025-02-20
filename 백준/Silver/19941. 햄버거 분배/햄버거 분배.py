def max_h(N, K, table):
    people = []
    burgers = []

    for i in range(N):
        if table[i] == 'P':
            people.append(i)
        elif table[i] == 'H':
            burgers.append(i)

    p_index, h_index = 0, 0
    count = 0

    while p_index < len(people) and h_index < len(burgers):
        if abs(people[p_index] - burgers[h_index]) <= K:
            count += 1
            p_index += 1
            h_index += 1
        elif people[p_index] < burgers[h_index]:
            p_index += 1
        else:
            h_index += 1

    return count

N, K = map(int, input().split())
table = input().strip()

print(max_h(N, K, table))