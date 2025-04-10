def min_num(N, num):
    if N == 1:
        return sum(num) - max(num)
    
    one_min = min(num)
    two_min = min(num[i] + num[j] for i, j in arr_2)
    three_min = min(num[i] + num[j] + num[k] for i, j, k in arr_3)

    num_three = 4
    num_two = 4 * (N - 2) + 4 * (N - 1)
    num_one = (N - 2) * (N - 2) + (N - 2) * 4 * (N - 1)

    return (
        three_min * num_three +
        two_min * num_two +
        one_min * num_one
    )

N = int(input())
num = list(map(int, input().split()))

arr_2 = [
    (0, 1), (0, 2), (0, 3), (0, 4),
    (5, 1), (5, 2), (5, 3), (5, 4),
    (1, 2), (2, 4), (4, 3), (3, 1)
]

arr_3 = [
    (0, 1, 2), (0, 2, 4), (0, 3, 4), (0, 1, 3),
    (5, 1, 2), (5, 2, 4), (5, 4, 3), (5, 3, 1)
]

print(min_num(N, num))