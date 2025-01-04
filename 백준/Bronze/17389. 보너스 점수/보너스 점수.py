test_num = int(input())
count_arr = list(input())
bonus = 0
score = 0

for i in range(1, test_num+1):
    if count_arr[i-1] == "O":
        score += (i + bonus)
        bonus += 1
    else:
        bonus = 0

print(score)