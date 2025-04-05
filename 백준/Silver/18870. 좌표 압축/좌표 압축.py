import sys

input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

arr = sorted(set(X))

# 값 → 인덱스 매핑
answer = {num: i for i, num in enumerate(arr)}

# 압축 결과 출력
print(' '.join(str(answer[x]) for x in X))
