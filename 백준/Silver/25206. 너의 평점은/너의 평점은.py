score = 0
max_score = 0
sub_score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0}

for i in range(20):
    arr = input().split()
    if arr[2] != 'P':
        score += (float(arr[1]) * sub_score[arr[2]])
        max_score += float(arr[1])

print(f"{score / max_score:.6f}")