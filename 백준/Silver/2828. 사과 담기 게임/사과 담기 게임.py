N, M = map(int, input().split())
J = int(input())

left = 1
right = M
move = 0

for _ in range(J):
    apple = int(input())
    if apple < left:
        move += left - apple
        right -= (left - apple)
        left = apple
    elif apple > right:
        move += apple - right
        left += (apple - right)
        right = apple

print(move)